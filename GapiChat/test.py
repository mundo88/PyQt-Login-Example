import requests,json


USER_ACCESS_TOKEN ="EAAHF8bZCDts4BAIWSZANxnHQhKTRNorDpntpKalVVpWyiqCCQbUfXZBlrYfxoaLsUZB1sziFSFXdZCfav7GBvjEKnZAzrQYphXRGOcOArZCjIFzLs5WMs1LaeFFpukYxQ3bOJMNlWsmAQ49YjD6RN8WLMbnsGiRs3MAAYOpDZB1AxgZDZD"
USER_ID = "100081469447185"
ACCESS_TOKEN_PAGE_URI = F"https://graph.facebook.com/{USER_ID}/accounts?fields=name,access_token&access_token=" + USER_ACCESS_TOKEN
COOKIE = "sb=uUSnYtLszVr9FLy1hUzJKHs3; datr=uUSnYvvbkOi7voLyr_vNaBxf; _fbp=fb.1.1661598248597.1032423279; c_user=100081469447185; m_page_voice=100081469447185; cppo=1; dpr=1; xs=45:_4HzlLhSqXGigw:2:1663594848:-1:6282::AcWXqlir2Hwc-4c5df3507fGWThhP7xPQC9UdJFdlqc; wd=1920x961; fr=0XmW0jDEkoToyBNDC.AWWbTUZXAlQIPE839D4CbBBxv18.BjOUlN.Eq.AAA.0.0.BjOU4G.AWXeoyUCCE4; usida=eyJ2ZXIiOjEsImlkIjoiQXJqM3ljNTFieDg5N3QiLCJ0aW1lIjoxNjY0NzAwMDkzfQ==; presence=EDvF3EtimeF16647B93EuserFA21B81469447185A2EstateFDutF0CEchF_7bCC"

rq = requests.Session()
# data_page = rq.get(url=ACCESS_TOKEN_PAGE_URI,headers={"cookie":COOKIE})
# print(data_page.json())

page_data = {
    'data': 
    [
        {
            'name': "Dom Setup's", 
            'access_token': 'EAAHF8bZCDts4BAO2f39avFZAn3LlhGL3KXTMZCO14EM3WFuGyJZCxiqQZCitAyOPaWsL1YD6VHPYFFHNDPRQ2n3EBFZBRHMef0uMZC80rmSpl5nVA92x2gfPC57wR31HaGZBrvZCwwjZBvvyqzU2xGAXNiLWUvOAm3fmSZAuR8ggfVaRx4BRZAZAZCCEFgwtuMRzpwBAPChpSLGUoyGmIwzJc77Dyq', 
            'id': '100604865231343'
        }, 
        {
            'name': 'Dom Neon', 
            'access_token': 'EAAHF8bZCDts4BAEIiH5FVrZBNNBlZBrOy81OMN5WRZCo7IUGDkFpZCfFdbyddXQF6yhUSXEirX0MehZCqMr2ZBaLyxjU7Vq4EHv5nDCrHpT22kFxw3WN7VzzprGMfgOXgcKXR0RgbpFpFXmIaJp1noA8DACicEIzAwaUDpBFcrq3TIQEh0ajzlgejU3SezQl9kAc1acyZAK40fH2qCnF5QdV', 
            'id': '100718325788739'
        }, 
        {
            'name': 'DOM - Biển LED ấn tượng', 
            'access_token': 'EAAHF8bZCDts4BAEe9b0YmpqCfZAttSWfpKJsy2zNnNwour3GT2hwLFBLwjrdWqMoNp3yjxJvsLg2TC7eVGLE7gvUS7EvP8FgiZCtzpcpTk3QehZByhoCmB6ZCAaT13nIbpv128WqyvLGScYHDzIjrCHhIs8kfgvUKN5SSu19u9ctNQZAjmeLaNKOeZCDLziSdbwPgahYG2CwiR0Wt6BKPB2', 
            'id': '102031679204310'
        }, 
        {
            'name': 'D O M', 
            'access_token': 'EAAHF8bZCDts4BAPmAiZBnTfVfmW3Cx4JBdyY5xwdcmFz8bodQJ5uuBJZCo83I51KIE81s0vPpiMtjargqZBbkQ7fjsZBZBJ7uke8hS64DlR1OokmWtLXiI50qwsO7oVONbZCaalQYzb5CPMZCTPXIxJsh4zOdus9OEgeCf4fn2VJrQsMhav9WDibhkVRVYXAs4ONvenxOXQskudSrpEPzZBuY', 
            'id': '253889015390115'
        }
    ]
}

for page in page_data['data']:
    list_msg_page = rq.get(url="https://graph.facebook.com/"+page['id']+"/conversations?access_token="+page['access_token'],headers={"cookie":COOKIE}).json()
    with open("jsontest.json","a",encoding="utf-8") as f:
        data = json.dumps(list_msg_page, indent=4)
        f.write(data)
        print(data)
