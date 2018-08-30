import requests
import pandas as pd
import time
url = "https://www.zhihu.com/api/v4/members/excited-vczh/followees"

querystring = {"include":"data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics","offset":"60","limit":"20"}

headers = {
    'cookie': "d_c0=\"AIBC9_hCrQuPTr_3oQudXDK4OQmMAPCjX1M=|1493385950\"; _zap=fb78805e-67aa-438f-a83a-2639bdd46e71; q_c1=41ea2242bf0a4b49aedd34a977ae3d7a|1506829340000|1493385950000; __DAYU_PP=Ib6j62uaeZfMMuiaUeQEffffffff822a17d500cd; z_c0=\"2|1:0|10:1526436918|4:z_c0|92:Mi4xQU14VkFnQUFBQUFBZ0VMMy1FS3RDeVlBQUFCZ0FsVk5OdUxvV3dDejdYMmhHYm84LWc1N0JtNmdqeVRSOXRuWFVn|df01001953ca33f5d4d9f45630fd835d5c8c9069bb1a8696f323e023124c26a6\"; __utma=51854390.1291609016.1534424109.1534424109.1534424109.1; __utmz=51854390.1534424109.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20151129=1^3=entry_date=20151129=1; q_c1=41ea2242bf0a4b49aedd34a977ae3d7a|1535439751000|1493385950000; _xsrf=126a54b3-ad53-4e02-8f9f-c6c58a0c6028; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8",
    #'x-udid': "AIBC9_hCrQuPTr_3oQudXDK4OQmMAPCjX1M=",
    #'x-requested-with': "fetch",
    #'pragma': "no-cache",
    #'x-ab-param': "se_syn=0;top_tag_isolation=1;top_feedre_cpt=101;top_gr_topic_reweight=0;se_entity=off;top_follow_reason=0;top_user_gift=0;top_yc=0;top_billread=1;top_nad=1;se_gemini_service=0;ls_play_continuous_order=1;top_billvideo=0;top_feedre=1;top_feedre_rtt=41;top_multi_model=0;top_newfollow=0;top_ntr=1;top_gr_model=0;top_hca=0;top_adpar=0;top_followtop=1;top_root=1;top_root_few_topic=0;top_root_mg=1;top_an=0;top_nid=5;top_billpic=0;top_dtmt=2;se_major_onebox=major;top_root_ac=1;se_gi=0;top_uit=0;top_ebook=0;top_card=-1;top_feedtopiccard=0;top_mlt_model=0;top_pfq=2;top_30=0;se_wiki_box=0;top_billupdate1=0;top_nszt=0;top_test_4_liguangyi=1;top_tmt=0;top_video_fix_position=0;top_billupdate=0;top_alt=0;top_is_gr=0;top_retag=0;top_video_rew=0;top_sj=2;top_nmt=0;se_minor_onebox=nd;se_tf=1;top_nuc=0;top_retagg=2;top_topic_feedre=21;top_gif=0;top_login_card=1;top_hqt=0;top_recommend_topic_card=0;top_universalebook=1;top_bill=0;top_free_content=-1;top_billab=1;top_new_user_gift=0;top_recall=3;top_yhgc=0;web_ask_flow=exp_a;pin_ef=orig;top_hweb=0;top_lowup=1;top_nucc=3;top_tffrt=0;top_feedre_itemcf=31;top_f_r_nb=1;se_dt=1;top_fqa=0;top_gr_auto_model=0;top_memberfree=1;top_sjre=0;top_keyword=0;top_tagore=1;top_cc_at=-1;top_root_web=0;top_tr=0;pin_efs=orig;top_billboard_count=1;top_keywordab=0;web_logoc=blue;top_vdio_rew=0;tp_sft=a",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    #'x-zse-84': "_krmQO5kQ_NbPkrlgg9k0WPkP98uAp8xgwAxNKPwP1ra7xAwlouxQW_xLc8uLgux",
    #'accept': "*/*",
    #'cache-control': "no-cache",
    #'authority': "www.zhihu.com",
    #'referer': "https://www.zhihu.com/people/excited-vczh/following?page=3",
    #'x-zse-83': "3_1.1",
    #'postman-token': "3f4bdc28-f747-9058-0a37-c5d69ca79a37"
    }
user_data = []

def get_user_data(page):
    for i in range(page):
        querystring['offset'] = i * 20
        response = requests.request("GET", url, headers=headers, params=querystring).json()['data']
        user_data.extend(response)
        print('正在爬取第%s页' % str(i+1))
        time.sleep(1)


if __name__=='__main__':
    get_user_data(10);
    df = pd.DataFrame.from_dict(user_data)
    # print(df.head())
    # print(response.text)
    df.to_csv('user.csv')