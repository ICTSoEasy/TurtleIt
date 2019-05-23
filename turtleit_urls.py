'''List of possible URLs'''

#urls[challenge][team]

class URL:
  def __init__(self,challenge,team,url):
    self.challenge = challenge
    self.team = team
    self.url = url
  def getUrl(self,challenge,team):
    if challenge == self.challenge and team == self.team:
      return self.url
    else:
      return False

def geturl(challenge,team):
  for url in urls:
    if (url.getUrl(challenge,team)):
        return url.getUrl(challenge,team)
  return False
      
urls = []

#Challenge 0
urls.append(URL(0,0,'https://docs.google.com/document/d/1UG8Ko_TmmkOrGqVPQJJsAIH9oGC7yDOOHadCSw3rkH0/edit?usp=sharing'))
urls.append(URL(0,1,'https://docs.google.com/document/d/1RcpyiETXzjahA0D2_u_PiMIaBjgAeISi4PClCQbsnZE/edit?usp=sharing'))
urls.append(URL(0,2,'https://docs.google.com/document/d/18jrp3WbOIW5-NxfFaZ31MODl5VugDne4IltbEA27Ydo/edit?usp=sharing'))
urls.append(URL(0,3,'https://docs.google.com/document/d/1nAd22Ft5vIroKvRWkzk55NpZmZyin0PDTEaI235Vto0/edit?usp=sharing'))
urls.append(URL(0,4,'https://docs.google.com/document/d/1w0UafS1UIJD9MB76t8jN5MTrA5m5PvJxzzSDEi4L0zM/edit?usp=sharing'))
urls.append(URL(0,5,'https://docs.google.com/document/d/1URnu9tU50_xOMXzQb46V9HS93dFZgn1vc9TBnYEHxks/edit?usp=sharing'))
urls.append(URL(0,6,'https://docs.google.com/document/d/1fwj9Z04VUyLAn0rpKoj9_H_9n7vSfVnOcNvxlm3-QU4/edit?usp=sharing'))
urls.append(URL(0,7,'https://docs.google.com/document/d/1cGL4ctotihz6tg_4g2ddb5NCHId_1bUakeWtwHGyU6k/edit?usp=sharing'))
urls.append(URL(0,8,'https://docs.google.com/document/d/1X7j2s1IcMc-FaPgIb_3cro_FQXJoWILbGVDy8GQgYQY/edit?usp=sharing'))
urls.append(URL(0,9,'https://docs.google.com/document/d/1umnCHi1JRaNAAsiV_ZGeHlnEvMPyWJbqULyUngMCHz8/edit?usp=sharing'))
urls.append(URL(0,10,'https://docs.google.com/document/d/1gvGJJCAQPErto7r9wGXrJde-W86NyLFAvuyLQQfX8EE/edit?usp=sharing'))
urls.append(URL(0,11,'https://docs.google.com/document/d/1yKoiSp6vhO1yDToWcj1FfyXQlAHpwwn-bt3X0OwS9cA/edit?usp=sharing'))
urls.append(URL(0,12,'https://docs.google.com/document/d/1ZrP1zJYiDVK6zSmHFBKopJyUa7nScz5kBd3rZ91kVNI/edit?usp=sharing'))
urls.append(URL(0,13,'https://docs.google.com/document/d/1vpCSV1u8d-T3vXJHWvnHx9XHzsSIavRjPFCnwav2laY/edit?usp=sharing'))
urls.append(URL(0,14,'https://docs.google.com/document/d/1z3owFCN7DewaV7G7_6_x-MuIdnJTwLzMHry418eQ2SA/edit?usp=sharing'))
urls.append(URL(0,15,'https://docs.google.com/document/d/1vlckPWgM1S-cftU4iEe_ZCZtQmOMhURodxZdc-PHlU0/edit?usp=sharing'))
urls.append(URL(0,16,'https://docs.google.com/document/d/1LQrnEMpybIUmkLFDDhH0skibvNTAVyelvGR3m4fQW-c/edit?usp=sharing'))
urls.append(URL(0,17,'https://docs.google.com/document/d/1f7nFu8DzjEaZm41eumrLUo0IrLUqT8zIZtPJDkqd8e8/edit?usp=sharing'))
urls.append(URL(0,18,'https://docs.google.com/document/d/18DUvqyVthni3uNsHvJ08xtAZw1-8h_GxGi9H15eZ5xg/edit?usp=sharing'))
urls.append(URL(0,19,'https://docs.google.com/document/d/1SKoERJ1YR7psyxVm_zKGBRNFXUgrR93wu7xfahsYfZc/edit?usp=sharing'))
urls.append(URL(0,20,'https://docs.google.com/document/d/1D2rHadoAc7TVgnvbBv-v9S2tnQSiNVuuMU8ehv1Wq7Y/edit?usp=sharing'))
urls.append(URL(0,21,'https://docs.google.com/document/d/1PSjSsMKZs4idLECcDfGFdz1-sVID-WveZ--kBuWb3bY/edit?usp=sharing'))
urls.append(URL(0,22,'https://docs.google.com/document/d/1sz2mbaGc8sMqORfLkRswYh_oeCAgL3ixrSt-AU77VYs/edit?usp=sharing'))
urls.append(URL(0,23,'https://docs.google.com/document/d/1n-zfpQqFR9xiXBV89rnrQCw7TdLJ9O5zVtNwcwa2k88/edit?usp=sharing'))
urls.append(URL(0,24,'https://docs.google.com/document/d/1oXN8Onno8cuUendb-JTI1Cep_P8FIJIlIUabEzy4W_A/edit?usp=sharing'))
urls.append(URL(0,25,'https://docs.google.com/document/d/13FPW7XnWJure7xQIX5N_WDBTGmKOHBfZi-cE7DYlYd4/edit?usp=sharing'))
urls.append(URL(0,26,'https://docs.google.com/document/d/1_c0HEifmrFUeRhA_vHumwIBD9dSG7x3Z3t3IG7_yMFM/edit?usp=sharing'))
urls.append(URL(0,27,'https://docs.google.com/document/d/1I8Qf6DY3ogjvfg_IbpPJSJtYqCvmu35Y3usEQG4e6yM/edit?usp=sharing'))
urls.append(URL(0,28,'https://docs.google.com/document/d/1Cub_jXr9yYyzVkHeQHYCsoDTIUAMO2CRLDFy7vL_ODI/edit?usp=sharing'))
urls.append(URL(0,29,'https://docs.google.com/document/d/1ulynj_ZNRiUmPh75mwwYLKjy5MCLxu-T2ghpFznAZ1c/edit?usp=sharing'))
urls.append(URL(0,30,'https://docs.google.com/document/d/179ke7faQWBdaFhrXtJTeQZXVJ1T5SsScgM8zii4UyFU/edit?usp=sharing'))
urls.append(URL(0,31,'https://docs.google.com/document/d/16MchMrREBYY-U6fw24m8fgu6QIEBIPLcVd3CaWLL_gQ/edit?usp=sharing'))
urls.append(URL(0,32,'https://docs.google.com/document/d/1Jb4st_ud2UXmRGdQT-DNrDc52eA_9RkUT2wS3h8TsF0/edit?usp=sharing'))
urls.append(URL(0,33,'https://docs.google.com/document/d/10W9WSpvmNkbpUB3hYZRhod0wE15VCIM_UJtGJx2mwjk/edit?usp=sharing'))
urls.append(URL(0,34,'https://docs.google.com/document/d/1cDcPNeWFAgiZdJOXgtRaERRnJHpJSnb8jNZyIET1uNg/edit?usp=sharing'))
urls.append(URL(0,35,'https://docs.google.com/document/d/1jVmJhtYP2NtGKTd2UVuX_8zcuTs5QUTjnvPdk7Zyx50/edit?usp=sharing'))
urls.append(URL(0,36,'https://docs.google.com/document/d/1bgWhrKHnHLdYFeJnyMnTaEDw1kCKdLpxjU-5o616k74/edit?usp=sharing'))
urls.append(URL(0,37,'https://docs.google.com/document/d/18Y3EMozwnZpSX5Mv7p7Mp83kMIXFr3R7BMtksfhvknU/edit?usp=sharing'))
urls.append(URL(0,38,'https://docs.google.com/document/d/18MgusSCyB6wgE7-mySwKuufNFlRT6wLPXZ1C6AwQG7I/edit?usp=sharing'))
urls.append(URL(0,39,'https://docs.google.com/document/d/1BHjSSs6svdH8to7yg3RNP6vaSd0mOk9fmL9FTTX8VGE/edit?usp=sharing'))
urls.append(URL(0,40,'https://docs.google.com/document/d/124HCEObtXHYrxLvXmIM_NH4AwrwxKPx4CHwN58MT_k8/edit?usp=sharing'))
urls.append(URL(0,41,'https://docs.google.com/document/d/13ACupe90aHm_PmfFrh0ixOQM5kJpz-ECDNn_VHJDlZA/edit?usp=sharing'))
urls.append(URL(0,42,'https://docs.google.com/document/d/1n8BsTv53RdMrmUEoW046XW-5uFlD2j2O7yNkmX4Ccm0/edit?usp=sharing'))
urls.append(URL(0,43,'https://docs.google.com/document/d/1Plrbzxqb0vps6JFIEPtGZUTivdUFEqOqbS-cfNYlHak/edit?usp=sharing'))
urls.append(URL(0,44,'https://docs.google.com/document/d/1o_X5Uyb9okCgnd8SiFcW-00duBm_qzojPfaoEorOFCk/edit?usp=sharing'))
urls.append(URL(0,45,'https://docs.google.com/document/d/1luOeUr19gk0ztvJhtF2NPoLFpUkGKUxxljjdsOMdzBI/edit?usp=sharing'))
urls.append(URL(0,46,'https://docs.google.com/document/d/1NvBUj36-jPYtmkg-8TAtFHrLvJxGrXnrN-x-1wjF69M/edit?usp=sharing'))
urls.append(URL(0,47,'https://docs.google.com/document/d/1dqJCSlfFXJKu5IjfIdwXrrQFpb9lJJLAqCXskyC8gaI/edit?usp=sharing'))
urls.append(URL(0,48,'https://docs.google.com/document/d/1z-lCSP4SpzYxtB7CW4L8NqloXgQatJDCtUyi3sEZGig/edit?usp=sharing'))
urls.append(URL(0,49,'https://docs.google.com/document/d/1k0sBB3GJI_TfPfelcFDfNH4II0EhQs8-oCDGdTdDFGE/edit?usp=sharing'))
urls.append(URL(0,50,'https://docs.google.com/document/d/12nBxQh8154U_he-U4KIQas1z2nc4a1TeECB3Qy00naY/edit?usp=sharing'))
urls.append(URL(0,51,'https://docs.google.com/document/d/1A577BhzhGfbKc07Em689u27JbY5I8_nx-Z5RQAGMZfg/edit?usp=sharing'))
urls.append(URL(0,52,'https://docs.google.com/document/d/1IdIvkXiRdNKW416yGwsXUQUrf6VWwuPsYut3spWoQjg/edit?usp=sharing'))
urls.append(URL(0,53,'https://docs.google.com/document/d/1fmpKiIdW4z07KgaTIzmOrtFUzz056jO0W1J2jk_2770/edit?usp=sharing'))
urls.append(URL(0,54,'https://docs.google.com/document/d/1DrXZiNWRoY1R0uT6LwyWfKox3TiHb9vvchgnSsv_9tM/edit?usp=sharing'))
urls.append(URL(0,55,'https://docs.google.com/document/d/1kSSKzs4vqJJ3tCUM9yhHFsXODaHkmkxrgclulR4LBKQ/edit?usp=sharing'))
urls.append(URL(0,56,'https://docs.google.com/document/d/1TsQJP0ntwfyhRBmGFPJAvOOBkVfRPp3By52CRsvdfHc/edit?usp=sharing'))
urls.append(URL(0,57,'https://docs.google.com/document/d/1_Jrf3K1C-OOQ8QKI-58MPOOrywmu60YSQhhzOx-pQ_I/edit?usp=sharing'))
urls.append(URL(0,58,'https://docs.google.com/document/d/1xCHFAhZlPuIwe57JB4GyiIaeBOyidWg7qWjKkcUJwSQ/edit?usp=sharing'))
urls.append(URL(0,59,'https://docs.google.com/document/d/1JOwUSJo2_LcOS0j8hQxWneXQWGOBsXQRThIcxTt1eIc/edit?usp=sharing'))
urls.append(URL(0,60,'https://docs.google.com/document/d/1cWNhtrCrE1p7_c2cNEcAnLR9dqFGIwn2FvNuI3l7GEo/edit?usp=sharing'))
urls.append(URL(0,61,'https://docs.google.com/document/d/1uWVgwNaU0l30f4DuzaALx4TKoQ3xbnNVxqBDnZ3m-LU/edit?usp=sharing'))
urls.append(URL(0,62,'https://docs.google.com/document/d/1QG-Xfo--NPLj_pn6ykpZZe-QskNr_ssHiBQl6WyKn0I/edit?usp=sharing'))
urls.append(URL(0,63,'https://docs.google.com/document/d/1Q94-p7v_I3XrDRioRhd1TZbAHWgt1p-mdM42JBSiY6o/edit?usp=sharing'))
urls.append(URL(0,64,'https://docs.google.com/document/d/1BMZh-IpgevMA4O4LK6YiFVVGHfNwmUBTymrFgK2wes8/edit?usp=sharing'))
urls.append(URL(0,65,'https://docs.google.com/document/d/1_2cJl-d99fadhCC_XZvq1GcKzcJ3qFZ70B4NZBHM-ko/edit?usp=sharing'))
urls.append(URL(0,66,'https://docs.google.com/document/d/1hqhdnnUXSCwwZ5nc4zUeDHur3JNPtI17J1WXlhh529M/edit?usp=sharing'))
urls.append(URL(0,67,'https://docs.google.com/document/d/1T48W1oRQheuA9cp4tB1xmG10ynUZWTYm6NLBVlSqHt4/edit?usp=sharing'))
urls.append(URL(0,68,'https://docs.google.com/document/d/1Gon8McE_zI0EkcdP6jNVDHYnJ3EFxova6IGkSrF0SmI/edit?usp=sharing'))
urls.append(URL(0,69,'https://docs.google.com/document/d/19yKvDrk22rb9N9A-ZnKErhaCsVdImXOKlz3NyWa95gw/edit?usp=sharing'))
urls.append(URL(0,70,'https://docs.google.com/document/d/14E4ZlAnA7rrHDfWqRZw6xUn0mILiTitDFB9hAy5t6k8/edit?usp=sharing'))
urls.append(URL(0,71,'https://docs.google.com/document/d/1Zjv18oBri-d0TssajcGzrGGfh_JE3TMeWlxbzQtT8dI/edit?usp=sharing'))
urls.append(URL(0,72,'https://docs.google.com/document/d/1AjSPyW1h1lKbQ5l0p_b7atyzrwZeHbTAVng6Veq28Vs/edit?usp=sharing'))
urls.append(URL(0,73,'https://docs.google.com/document/d/1sPORlMgiM-uI3zI2YFGdwZy59mxGMPltgh3-WKxGHwY/edit?usp=sharing'))
urls.append(URL(0,74,'https://docs.google.com/document/d/1zTLGOCTmOnaCy122144fVvDGIM1lMfGrrd6B1tYPiME/edit?usp=sharing'))