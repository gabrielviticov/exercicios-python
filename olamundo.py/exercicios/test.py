import webbrowser

site = webbrowser.open_new_tab('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi89_i1yfPvAhVqHbkGHWlXCO8QFjAAegQIAhAE&url=https%3A%2F%2Fwww.google.com.br%2Fmaps&usg=AOvVaw3cFx2-7_OaqMQ-d44zdcXo')
viagem = float(input('\nDigite a quilometragem percorrida em sua viagem: '))
calculo1 = viagem * 0.50
calculo2 = viagem * 0.45
if viagem <= 200:
 print('Para realizar o trajeto de {:.1f}km\nO valor que você pagará na passagem será de R$ {:.2f}'.format(viagem,calculo1))
else:
 print('Para realizar o trajeto de {:.1f}km\nO valor que você pagará na passagem será de R$ {:.2f}'.format(viagem,calculo2))