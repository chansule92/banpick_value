df_list=[]
for game in game_list_df['Game_ID'].values:
    Blue_Team=result[game]['BLUE'][0]
    Red_Team=result[game]['RED'][0]
    temp_list=[]
    for k in Blue_Team:
        try:
            Ban=max(df[df['Champion']==k]['Ban'])
        except ValueError:
            Ban=0
        try:
            Pick=max(df[df['Champion']==k]['Pick'])
        except ValueError:
            Pick=0
        try:
            Win_rate=max(df[df['Champion']==k]['Win_rate'])
        except ValueError:
            Win_rate=0
        Duo_score=0
        Count_score=0
        for i in Blue_Team:
            if k==i:
                pass
            else :
                if len(df[(df['Champion']==k)&(df['con_champ']==i)]['Duo_Score']) == 0:
                    pass
                else:
                    try:
                        Duo_score = Duo_score + float(df[(df['Champion']==k)&(df['con_champ']==i)]['Duo_Score'].iloc[0])
                    except IndexError:
                        Duo_score = 0
        for j in Red_Team:
            if k==j:
                pass
            else :
                if len(df[(df['Champion']==k)&(df['con_champ']==j)]['Count_Score']) == 0:
                    pass
                else:
                    try:
                        Count_score = Count_score+ float(df[(df['Champion']==k)&(df['con_champ']==j)]['Count_Score'].iloc[0])
                    except IndexError:
                        Count_score = 0
        temp_list.append([Ban,Pick,Win_rate,round(Duo_score,2),round(Count_score,2)])
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    for i in temp_list:
        sum1+=i[0]
        sum2+=i[1]
        sum3+=i[2]
        sum4+=i[3]
        sum5+=i[4]
    final_list=[sum1,sum2,sum3,sum4,sum5]
    
    for k in Red_Team:
        try:
            Ban=max(df[df['Champion']==k]['Ban'])
        except ValueError:
            Ban=0
        try:
            Pick=max(df[df['Champion']==k]['Pick'])
        except ValueError:
            Pick=0
        try:
            Win_rate=max(df[df['Champion']==k]['Win_rate'])
        except ValueError:
            Win_rate=0
        Duo_score=0
        Count_score=0
        for i in Red_Team:
            if k==i:
                pass
            else :
                if len(df[(df['Champion']==k)&(df['con_champ']==i)]['Duo_Score']) == 0:
                    pass
                else:
                    try:
                        Duo_score = Duo_score + float(df[(df['Champion']==k)&(df['con_champ']==i)]['Duo_Score'].iloc[0])
                    except IndexError:
                        Duo_score = 0
        for j in Blue_Team:
            if k==j:
                pass
            else :
                if len(df[(df['Champion']==k)&(df['con_champ']==j)]['Count_Score']) == 0:
                    pass
                else:
                    try:
                        Count_score = Count_score+ float(df[(df['Champion']==k)&(df['con_champ']==j)]['Count_Score'].iloc[0])
                    except IndexError:
                        Count_score = 0
        temp_list.append([Ban,Pick,Win_rate,round(Duo_score,2),round(Count_score,2)])
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    sum5=0
    for i in temp_list:
        sum1+=i[0]
        sum2+=i[1]
        sum3+=i[2]
        sum4+=i[3]
        sum5+=i[4]
    final_list.append(sum1)
    final_list.append(sum2)
    final_list.append(sum3)
    final_list.append(sum4)
    final_list.append(sum5)
    final_list.append(result[game]['BLUE'][1])
    df_list.append(final_list)
ml_df=pd.DataFrame(df_list)
ml_df.columns=['Blue_Ban','Blue_Pick','Blue_rate','Blue_Duo_Score','Blue_Count_Score','Red_Ban','Red_Pick','Red_rate','Red_Duo_Score','Red_Count_Score','Blue_Result']                                                                                                                                                                                
