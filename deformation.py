"""Définition de la fonction deformation pour le projet Vasarely
"""
def deformation(p, c, r):
    """Calcule la déformation du point p étant donné la sphère de centre c et de rayon r
    Données: p (triple), c (triple), r (float)
    Résultat : (tuple) point après déformation"""
    from math import pi, asin, sin, cos

    EPS = 1.0e-5  # calculs fait à EPS près

    def point_d_intersection(p_i, c_i, r_i):
        """ Hypothèses : p_i et c_i non verticaux
        Résultat : plus proche point d'intersection du plan vertical qui passe par c_i et p_i
                      avec la sphère de centre c_i et de rayon r_i et le plan z=0"""

        def racine_eq_sec_deg(a_e, b_e, c_e):
            """Calcul des racines de l'équation du second degré
            Données: coefficients de l'équation
            Résultat : tuple de float avec les 0, 1 ou 2 racines"""

            delta = b_e ** 2 - 4 * a_e * c_e
            if abs(delta) < EPS:
                res_rac = (-b_e / (2 * a_e),)
            elif delta < 0:
                res_rac = tuple()
            else:  # delta > 0
                res_rac = ((-b_e + delta ** 0.5) / (2 * a_e), (-b_e - delta ** 0.5) / (2 * a_e))
            return res_rac

        def inters_p_memes_abscisses(c_i, r_i):
            """plus proche point d'intersection du plan vertical qui passe par c_i et p_i
            avec la sphère de centre c_i et de rayon r_i et le plan z=0
            cas où p_i et c_i ont la même abscisse"""
            a_2 = 1
            b_2 = -2 * c_i[1]
            c_2 = c_i[1] ** 2 + c_i[2] ** 2 - r_i ** 2
            rac = racine_eq_sec_deg(a_2, b_2, c_2)
            if abs(rac[0] - p_i[1]) < abs(rac[1] - p_i[1]):
                pti = (p_i[0], rac[0], 0)
            else:
                pti = (p_i[0], rac[1], 0)
            return pti

        def intersect_memes_ordonnees(c_i, r_i):
            """plus proche point d'intersection du plan vertical qui passe par c_i et p_i
            avec la sphère de centre c_i et de rayon r_i et le plan z=0
            cas où p_i et c_i ont la même ordonnée"""
            a_2 = 1
            b_2 = -2 * c_i[0]
            c_2 = c_i[0] ** 2 + c_i[2] ** 2 - r_i ** 2
            rac = racine_eq_sec_deg(a_2, b_2, c_2)
            if abs(rac[0] - p_i[0]) < abs(rac[1] - p_i[0]):
                pti = (rac[0], p_i[1], 0)
            else:
                pti = (rac[1], p_i[1], 0)
            return pti

        def intersection_cas_general(p_i, c_i, r_i):
            """plus proche point d'intersection du plan vertical qui passe par c_i et p_i
            avec la sphère de centre c_i et de rayon r_i et le plan z=0
            cas général"""
            a_2 = c_i[1] - p_i[1]
            b_2 = p_i[0] - c_i[0]
            c_2 = -(b_2 * p_i[1] + a_2 * p_i[0])
            a_3 = b_2 ** 2 + a_2 ** 2
            b_3 = - 2 * b_2 ** 2 * c_i[0] + 2 * a_2 * c_2 + 2 * b_2 * c_i[1] * a_2
            c_3 = +b_2 ** 2 * c_i[0] ** 2 + c_2 ** 2 + b_2 ** 2 * c_i[1] ** 2\
                 + 2 * c_2 * b_2 * c_i[1] + b_2 ** 2 * (c_i[2] ** 2 - r_i ** 2)
            # solutions de l'équ du second degré
            rac = racine_eq_sec_deg(a_3, b_3, c_3)
            # prend la racine la plus proche de p_i
            if abs(rac[0] - p_i[0]) < abs(rac[1] - p_i[0]):
                pti = (rac[0], (a_2 * rac[0] + c_2) / -b_2, 0)
            else:
                pti = (rac[1], (a_2 * rac[1] + c_2) / -b_2, 0)
            return pti

        # code de point_d_intersection
        a_1 = c_i[1] - p_i[1]
        b_1 = p_i[0] - c_i[0]

        if abs(b_1) < EPS:  # même valeur d'abscisses x = c_i[0]
            pti = inters_p_memes_abscisses(c_i, r_i)

        elif abs(a_1) < EPS:  # même valeur d'ordonnées y = c_i[1]
            pti = intersect_memes_ordonnees(c_i, r_i)

        else:  # cas général p_i et c_i non alignés
            pti = intersection_cas_general(p_i, c_i, r_i)
               # point d'intersection de sphère plan z=0 et
               # plan vertical passant par c_i et p_i

        return pti

    def distance(p_1, p_2):
        """Calcule la distance euclidienne entre p_1 et p_2"""
        return ((p_2[0] - p_1[0]) ** 2 + (p_2[1] - p_1[1]) ** 2 \
                + (p_2[2] - p_1[2]) ** 2) ** 0.5

    # code de déformation
    over = c[2] > 0 # vrai si le centre de la sphère est au dessus du plan z=0
    c = (c[0], c[1], -abs(c[2]))  # place c sous le plan z=0 pour les calculs
    if distance(p, c) >= r:  # hors de la sphère de déformation
        res = p  # pas de déformation
    else:
        if abs(p[0] - c[0]) + abs(p[1] - c[1]) < EPS:  # p à la verticale de c
            res = (p[0], p[1], c[2] + r) # remonte p sur la sphère
        else:  # cas général
            pt_i = point_d_intersection(p, c, r)
            # pt_i = plus proche (de p) point d'intersection entre le plan vertical
            # passant par p et c et la sphère de déformation
            if abs(c[2]) < EPS:  # centre de la sphère sur le pavage
                alpha = pi / 2
            else:  # sphère sous le pavage
                sin_alpha = distance(pt_i, (c[0], c[1], 0)) / r
                alpha = asin(sin_alpha)
            rapport = distance((c[0], c[1], 0), p) / distance((c[0], c[1], 0), pt_i)
            beta = alpha * rapport
            x_2 = c[0] + (pt_i[0] - c[0]) * sin(beta) / sin(alpha)
            y_2 = c[1] + (pt_i[1] - c[1]) * sin(beta) / sin(alpha)
            z_2 = c[2] + r * cos(beta)
            res = (x_2, y_2, z_2)  # point après déformation
    if over:
        res = (res[0], res[1], -res[2])
        # remet le point au dessus du plan si c'était le cas initialement
    return res


if __name__ == "__main__":
    print(deformation((1, 2, 3), (0, 0, 0), 100))
