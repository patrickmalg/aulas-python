larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
#a cada 2m² é necessario 1L de tinta
tinta = area / 23
print('Para pintar essa parede você precisará de {}L de tinta.'.format(tinta))