import pandas as pd
import MySQLdb

# MySQL 연결 설정
game_list_query ="""SELECT Game_ID,Blue_Result, Red_Result
  FROM a_game
 WHERE League = 'LCK Spring 2024'"""

game_list_df = pd.read_sql(game_list_query, conn)


game_list=game_list_df['Game_ID'].to_list()
result={}
Team_div = ['BLUE','RED']
Position_div = ['TOP','JUNGLE','MID','ADC','SUPPORT']
result={}
for i in game_list:  
    team_id={}
    for j in Team_div:
        temp_list=[]
        if j =='BLUE':
            game_result=game_list_df[game_list_df['Game_ID']==i]['Blue_Result'].values[0]
        else :
            game_result=game_list_df[game_list_df['Game_ID']==i]['Red_Result'].values[0]
        for k in Position_div:
            champ_query="""SELECT Champion FROM a_game_stat where Game_ID = '{}' and Team_Div = '{}' and Role = '{}';""".format(i,j,k)
            champ_df=pd.read_sql(champ_query, conn)
            temp_list.append((champ_df['Champion'].values)[0])
            team_id[j]=[temp_list,game_result]
            result[i]=team_id

query = """
SELECT M1.Champion
     , M1.con_champ
     , MAX(M1.BP) AS BP
     , MAX(M1.Ban) AS Ban 
     , MAX(M1.Pick) AS Pick
     , MAX(M1.total_win_rate) AS Win_rate
     , CASE WHEN MAX(M1.duo_score) = 0 THEN min(M1.duo_score) ELSE Max(M1.duo_score) end AS Duo_Score
     , CASE WHEN MAX(M1.count_score) = 0 THEN Min(M1.count_score) ELSE max(M1.count_score) END AS Count_Score
  FROM ( SELECT M.Champion
              , M.con_champ
              , M.Team_YN
              , M.BP
              , M.Ban
              , M.Pick
              , M.total_win_cnt
              , M.total_win_rate
              , M.duo_play_cnt
              , M.duo_win_cnt
              , M.duo_win_rate
              , CASE WHEN Team_YN = 'Y' THEN M.duo_win_rate - M.total_win_rate ELSE 0 END AS duo_score
              , CASE WHEN Team_YN = 'N' THEN M.duo_win_rate - M.total_win_rate ELSE 0 END AS count_score
           FROM ( SELECT T1.Champion
                       , T2.con_champ
                       , T2.Team_YN
                       , T1.BP
                       , T1.Ban
                       , T1.Pick
                       , ifnull(T3.win_cnt,0) AS total_win_cnt
                       , ROUND(ifnull(T3.win_cnt,0)/T1.Pick*100,2) AS total_win_rate
                       , ifnull(T2.play_cnt,0) AS duo_play_cnt
                       , ifnull(T2.win_cnt,0) AS duo_win_cnt
                       , ROUND(ifnull(T2.win_cnt,0)/ifnull(T2.play_cnt,0)*100,2) AS duo_win_rate
                    FROM ( SELECT Champion
                                , count(Champion) AS BP
                                , SUM(CASE WHEN BP_DIV = 'Ban' THEN 1 ELSE 0 END) AS Ban
                                , SUM(CASE WHEN BP_DIV = 'Pick' THEN 1 ELSE 0 END) AS Pick
                             FROM ( SELECT 'Ban' AS BP_DIV
                                          , Ban AS Champion
                                       FROM a_game_ban
                                      UNION ALL 
                                     SELECT 'Pick' AS BP_DIV
                                          , Pick AS Champion
                                       FROM a_game_ban
                                  ) A
                            GROUP BY Champion
                         ) T1
                         LEFT OUTER JOIN 
                         ( WITH t1 AS
                           ( SELECT A.Game_ID
                                  , A.Champion
                                  , A.Team_Div
                                  , CASE WHEN A.Team_Div = 'Blue' THEN Blue_Result ELSE Red_Result END AS Result
                               FROM a_game_stat A
                                    INNER JOIN a_game B
                                 ON A.Game_ID = B.Game_ID 
                              WHERE A.Game_ID LIKE '%LCKSpring2024%'
                           )
                           SELECT A.Champion AS stan_champ
                                , B.Champion AS con_champ
                                , CASE WHEN A.Team_Div = B.Team_Div THEN 'Y' ELSE 'N' END AS Team_YN
                                , count(DISTINCT A.Game_ID) AS play_cnt
                                , count(DISTINCT CASE WHEN A.RESULT = 'Win' THEN A.Game_ID ELSE NULL END) AS win_cnt
                             FROM t1 A
                                  LEFT OUTER JOIN 
                                  t1 B
                               ON A.Game_ID = B.Game_ID
                              AND A.Champion != B.Champion
                            GROUP BY A.Champion
                                , B.Champion
                                , CASE WHEN A.Team_Div = B.Team_Div THEN 'Y' ELSE 'N' END 
                         ) T2
                      ON T1.Champion = T2.stan_Champ
                         LEFT OUTER JOIN
                         ( SELECT A.Champion 
                                , sum(CASE WHEN A.Team_Div = 'Blue' AND B.Blue_Result = 'Win' THEN 1
                                           WHEN A.Team_Div = 'Red' AND B.Red_result = 'Win' THEN 1 ELSE 0 END) AS win_cnt
                             FROM a_game_stat A
                                  INNER JOIN a_game B
                               ON A.Game_ID = B.Game_ID 
                            WHERE B.League = 'LCK Spring 2024'
                            GROUP BY A.Champion
                         ) T3
                      ON T1.Champion = T3.Champion
                ) M
          WHERE duo_play_cnt > 2
            AND BP > 9
       ) M1
 GROUP BY M1.Champion
      , M1.con_champ
"""
df = pd.read_sql(query, conn)
        
# 연결 종료
conn.close()
