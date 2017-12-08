zones = 'BK88,QN52,QN48,QN51,QN27,BX35,BX98,QN07,MN06,QN02,QN46,BK25,BX59,QN41,\
MN17,MN19,QN47,QN08,QN54,QN25,QN55,QN06,BK44,BK40,BK41,BK95,BX33,BK69,BX52,QN49,QN26,BK27,BK28,BK76,QN30,BK17,QN35,QN61,SI45,QN63,QN76,QN01,BX10,BK34,QN33,QN70,QN34,QN66,BK45,BK43,BK26,BK29,SI12,SI28,BK19,SI48,BK85,QN56,BK60,BK90,BK72,BK75,BK81,MN20,BK35,BK79,BK61,MN21,BK63,BK96,BX07,BX44,BX03,BX31,BK93,QN31,QN62,BK91,SI07,QN45,BK78,BK77,QN20,QN43,QN44,BX41,BK46,QN22,SI22,MN27,MN50,BX22,BX29,BK42,BX62,SI25,BX30,BX36,BX34,QN10,QN12,BX17,BX37,QN17,QN60,BK68,BX01,BX40,MN34,MN31,QN68,BX39,QN72,QN42,QN23,BX14,BX49,BX08,BX46,BX55,BX05,BX43,BX27,BX75,SI08,SI35,BX13,BK64,BK30,QN15,QN50,QN57,QN28,QN98,QN53,BK73,MN04,MN03,SI24,BK21,BK23,QN19,MN01,BX06,MN11,MN40,MN14,BX28,MN09,MN12,MN22,MN28,MN35,MN36,BX26,BX63,BX09,BX99,QN99,SI36,QN03,QN05,SI01,SI54,BK50,BK58,BK33,SI14,SI37,QN71,BK32,BK37,QN37,QN38,QN21,BK09,BK38,BK82,BK83,SI11,SI05,SI32,BK31,BK99,SI99,MN25,MN24,MN23,MN13,MN15,MN32,MN33,MN99,QN18,QN29'
split_zones = zones.split(',')

import pandas as pd

df = pd.read_csv('../data/geographic.csv')

with open('./test.json', 'w') as file:
    file.write('{"type":"FeatureCollection","features":[\n')
    for i, nbrhood in enumerate(df):
        if i == 0:
            boundary = df[nbrhood].as_matrix().reshape(int(df[nbrhood].size / 2),2)
            file.write('{"type":"Feature","properties":{'
                       '"name":"'+ split_zones[i] +'"},"geometry":{'
                        '"type":"Polygon","coordinates":[[')
            for k, j in enumerate(boundary):
                if k == 1:
                    file.write('[' + str(j[0]) + ',' + str(j[1]) + ']')
                elif str(j[0]) != 'nan':
                    file.write(',[' + str(j[0]) + ',' + str(j[1]) +']')

            file.write(']]}}\n')

    file.write("]}\n")