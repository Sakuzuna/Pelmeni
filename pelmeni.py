import colorama
from colorama import Fore
import sys
import csv
import select


#Кто не любит пельмени тот пидар

Red = Fore.RED 
Green = Fore.GREEN 
Blue = Fore.BLUE 
Yellow = Fore.YELLOW 
Reset = Fore.RESET 
White = Fore.WHITE 

print(f"""{Red}
                         .S_SsS_S.    .S_SSSs     .S_sSSs     .S    S.                                   
                        .SS~S*S~SS.  .SS~SSSSS   .SS~YS%%b   .SS    SS.                                  
                        S%S `Y' S%S  S%S   SSSS  S%S   `S%b  S%S    S&S                                  
                        S%S     S%S  S%S    S%S  S%S    S%S  S%S    d*S                                  
                        S%S     S%S  S%S SSSS%S  S%S    d*S  S&S   .S*S                                  
                        S&S     S&S  S&S  SSS%S  S&S   .S*S  S&S_sdSSS                                   
                        S&S     S&S  S&S    S&S  S&S_sdSSS   S&S~YSSY%b                                  
                        S&S     S&S  S&S    S&S  S&S~YSY%b   S&S    `S%                                  
                        S*S     S*S  S*S    S&S  S*S   `S%b  S*S     S%                                  
                        S*S     S*S  S*S    S*S  S*S    S%S  S*S     S&                                  
                        S*S     S*S  S*S    S*S  S*S    S&S  S*S     S&                                  
                        SSS     S*S  SSS    S*S  S*S    SSS  S*S     SS                                  
                                SP          SP   SP          SP                                          
                                Y           Y    Y           Y                                           
                                                                                                         
 .S_SSSs     .S       S.    .S_SSSs     .S_sSSs     .S  sdSS_SSSSSSbs    sSSs   .S    S.    .S   .S S.   
.SS~SSSSS   .SS       SS.  .SS~SSSSS   .SS~YS%%b   .SS  YSSS~S%SSSSSP   d%%SP  .SS    SS.  .SS  .SS SS.  
S%S   SSSS  S%S       S%S  S%S   SSSS  S%S   `S%b  S%S       S%S       d%S'    S%S    S&S  S%S  S%S S%S  
S%S    S%S  S%S       S%S  S%S    S%S  S%S    S%S  S%S       S%S       S%|     S%S    d*S  S%S  S%S S%S  
S%S SSSS%P  S&S       S&S  S%S SSSS%P  S%S    S&S  S&S       S&S       S&S     S&S   .S*S  S&S  S%S S%S  
S&S  SSSY   S&S       S&S  S&S  SSSY   S&S    S&S  S&S       S&S       Y&Ss    S&S_sdSSS   S&S   SS SS   
S&S    S&S  S&S       S&S  S&S    S&S  S&S    S&S  S&S       S&S       `S&&S   S&S~YSSY%b  S&S    S S    
S&S    S&S  S&S       S&S  S&S    S&S  S&S    S&S  S&S       S&S         `S*S  S&S    `S%  S&S    SSS    
S*S    S&S  S*b       d*S  S*S    S&S  S*S    S*S  S*S       S*S          l*S  S*S     S%  S*S    S*S    
S*S    S*S  S*S.     .S*S  S*S    S*S  S*S    S*S  S*S       S*S         .S*P  S*S     S&  S*S    S*S    
S*S SSSSP    SSSbs_sdSSS   S*S SSSSP   S*S    S*S  S*S       S*S       sSS*S   S*S     S&  S*S    S*S    
S*S  SSY      YSSP~YSSY    S*S  SSY    S*S    SSS  S*S       S*S       YSS'    S*S     SS  S*S    S*S    
SP                         SP          SP          SP        SP                SP          SP     SP     
Y                          Y           Y           Y         Y                 Y           Y      Y      
                                                                                                         
-------------------------------------------------------------------------------------------------------
#                                                                                                     #
#                                     <1> PEЦEIIT IIEЛbMEHEЙ                                          #
#                                                                                                     #
-------------------------------------------------------------------------------------------------------
{Reset}""")

input(f"Введите выбор")

if select == "1":
    print(f"    В муку добавляем соль, яйцо и растительное масло. Слегка перемешиваем. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №2 ")
print(f" Сдвигаем яйцо немного к краю миски, чтобы оно не сварилось. Заливаем муку горячей водой (температура 70-75 градусов), постоянно перемешивая ложкой. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №3 ")
print(f" Затем замешиваем тесто руками. Если останутся небольшие вкрапления сварившегося желтка - ничего страшного, они разойдутся при вымешивании теста. ")
print(f" Вымешиваем тесто примерно 7 минут, пока оно полностью не остынет. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №4 ")
print(f" Тесто не липнет ни к рукам, ни к поверхности, поэтому дополнительно муку можно не добавлять. ")
print(f" Накрываем тесто полотенцем и даём ему отдохнуть 20-30 минут. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №5 ")
print(f" Готовим начинку. Вес теста - приблизительно 800 г, поэтому и начинки берём тоже 800 г. ")
print(f" Мясо, сало и лук перемалываем с помощью мясорубки. (Можно взять уже готовый фарш и смешать с измельчённым луком. ")
print(f" Фарш солим и перчим. Добавляем немного воды, чтобы фарш был слегка жидковатым. Перемешиваем. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №6 ")
print(f" Берём часть теста весом 120 г, выкладываем на присыпанную мукой поверхность и раскатываем по размеру пельменницы. Остальное тесто отправляем под полотенце, чтобы оно не засыхало. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №7 ")
print(f" Хорошо посыпаем мукой верх пельменницы и ту сторону теста, которую будем выкладывать на пельменницу, чтобы пельмени хорошо от неё отделялись. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №8 ")
print(f" Разравниваем тесто по всей поверхности пельменницы. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №9 ")
print(f" Выкладываем фарш в ячейки. Следим, чтобы фарш не попадал на тесто вокруг ячеек, таким образом тесто будет хорошо скрепляться и пельмени не развалятся. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №10 ")
print(f" Раскатываем еще одну часть теста (весом 80 г), накрываем пельменницу, хорошо прокатываем скалкой. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №11 ")
print(f" Убираем остатки теста по краям, кладём под полотенце, их можно использовать повторно. Вытряхиваем пельмени из пельменницы. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №12 ")
print(f" Из этого количества теста и фарша получилось 185 пельменей (5 пельменниц). Пельмени выкладываем на посыпанную мукой поверхность и замораживаем. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №13 ")
print(f" Отвариваем пельмени в подсоленной воде с лавровым листом, горошинами чёрного перца и луком. Слегка перемешиваем пельмени и варим 2-3 минуты после того, как они всплывут. Даже если варить дольше, пельмени не разварятся. ")
print(f"  ")
print(f" Фото приготовления рецепта: Домашние пельмени - шаг №14 ")
print(f" Подаём пельмени со сливочным маслом. ")
print(f" Приятного аппетита! ")
exit()
