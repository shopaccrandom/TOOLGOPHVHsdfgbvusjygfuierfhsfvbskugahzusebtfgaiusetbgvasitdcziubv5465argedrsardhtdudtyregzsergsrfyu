import requests
import random
from time import sleep

# Mã màu
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\033[35m"
hong = "\033[1;95m"
xam = "\033[1;37;90m"
cam = "\033[1;38;2;255;165;0m"
xanhngoc = "\033[1;38;2;0;255;255m"
nau = "\033[1;38;2;139;69;19m"
vangnhat = "\033[1;38;2;255;255;224m"
hongdam = "\033[1;38;2;199;21;133m"
xanhlacay = "\033[1;38;2;34;139;34m"
xanhbienda = "\033[1;38;2;70;130;180m"

Domain = [
    'nguyenhoang', 'tranthanhhai', 'leminhkhanh', 'phamthanhdat', 'hoangtrungnghia', 
    'dangphucanh', 'vothithu', 'phanquanghuy', 'huynhngocmai', 'dothanhlong', 
    'buivananh', 'hothithao', 'ngominhhai', 'duongduckhanh', 'lythanhvinh', 
    'nguyenthithuy', 'tranvandung', 'lehoangnam', 'phamthithao', 'hoangminhchau', 
    'dangquangvinh', 'vovanthang', 'phanthingoc', 'huynhvanlong', 'dothithu', 
    'buiquanghuy', 'hovanmai', 'ngothanhdat', 'duongthithuy', 'lyvandung', 
    'nguyenhoanganh', 'tranminhhai', 'lethanhkhanh', 'phamvandat', 'hoangthithu', 
    'dangminhchau', 'vothanhvinh', 'phanquanghuy', 'huynhthithao', 'dovanlong', 
    'buithithuy', 'hovananh', 'ngothanhdat', 'duongminhhai', 'lythanhkhanh', 
    'nguyenvandung', 'tranhoangnam', 'lethithao', 'phamminhchau', 'hoangquangvinh', 
    'dangvanthang', 'vothithu', 'phanvandung', 'huynhhoanganh', 'dothanhdat', 
    'buiminhhai', 'hothanhkhanh', 'ngovananh', 'duongthithuy', 'lyhoangnam', 
    'nguyenthithao', 'tranminhchau', 'lequangvinh', 'phamvanthang', 'hoangthithu', 
    'dangvandung', 'vohoanganh', 'phanthanhdat', 'huynhminhhai', 'dothanhkhanh', 
    'buivananh', 'hothithuy', 'ngominhchau', 'duongquangvinh', 'lyvanthang', 
    'nguyenthithu', 'tranvandung', 'lehoanganh', 'phamthanhdat', 'hoangminhhai', 
    'dangthanhkhanh', 'vovananh', 'phanthithuy', 'huynhhoangnam', 'dothithao', 
    'buiminhchau', 'hoquangvinh', 'ngovanthang', 'duongthithu', 'lyvandung', 
    'nguyenhoanganh', 'tranminhhai', 'lethanhkhanh', 'phamvandat', 'hoangthithu', 
    'dangminhchau', 'vothanhvinh', 'phanquanghuy', 'huynhthithao', 'dovanlong', 
    'buithithuy', 'hovananh', 'ngothanhdat', 'duongminhhai', 'lythanhkhanh', 
    'nguyenvandung', 'tranhoangnam', 'lethithao', 'phamminhchau', 'hoangquangvinh', 
    'dangvanthang', 'vothithu', 'phanvandung', 'huynhhoanganh', 'dothanhdat', 
    'buiminhhai', 'hothanhkhanh', 'ngovananh', 'duongthithuy', 'lyhoangnam', 
    'nguyenthithao', 'tranminhchau', 'lequangvinh', 'phamvanthang', 'hoangthithu', 
    'dangvandung', 'vohoanganh', 'phanthanhdat', 'huynhminhhai', 'dothanhkhanh', 
    'buivananh', 'hothithuy', 'ngominhchau', 'duongquangvinh', 'lyvanthang', 
    'nguyenthithu', 'tranvandung', 'lehoanganh', 'phamthanhdat', 'hoangminhhai', 
    'dangthanhkhanh', 'vovananh', 'phanthithuy', 'huynhhoangnam', 'dothithao', 
    'buiminhchau', 'hoquangvinh', 'ngovanthang', 'duongthithu', 'lyvandung', 
    'nguyenminhlong', 'tranthanhvy', 'leductri', 'phamngocyen', 'hoangthanhbinh', 
    'dangthithao', 'vominhhung', 'phanvanphong', 'huynhthanhson', 'dothithuy', 
    'buiquangnam', 'hovanhoa', 'ngothanhlinh', 'duongminhtam', 'lythanhphuc', 
    'nguyenvanquan', 'tranthithu', 'lehoangduy', 'phamminhkhanh', 'hoangthanhthu', 
    'dangvanvinh', 'vothanhngoc', 'phanquangdung', 'huynhthithuy', 'dovananh', 
    'buithanhhai', 'hothanhdat', 'ngominhchau', 'duongthanhvinh', 'lyvanthang', 
    'nguyenthithu', 'tranvandung', 'lehoanganh', 'phamthanhdat', 'hoangminhhai', 
    'dangthanhkhanh', 'vovananh', 'phanthithuy', 'huynhhoangnam', 'dothithao', 
    'buiminhchau', 'hoquangvinh', 'ngovanthang', 'duongthithu', 'lyvandung', 
    'nguyenhoanganh', 'tranminhhai', 'lethanhkhanh', 'phamvandat', 'hoangthithu'
]

passw = [
'explanation1', 'hypothesize1', 'combination1', 'personality1', 'calculation1', 'destination1', 'exploration1', 'architecture1', 'university1', 'consequence1', 'possibility1', 'organization1', 'considerable1', 'protectional1', 'environment1', 'transmission1', 'measurement1', 'presentation1', 'exaggeration1', 'concentration1', 'examination1', 'illustration1', 'optimization1', 'contribution1', 'determination1', 'announcement1', 'capabilities1', 'publication1', 'observation1', 'registration1', 'expectations1', 'introduction1', 'transparency1', 'arrangement1', 'exploitation1', 'installation1', 'preparation1', 'coordination1', 'manipulation1', 'participation1', 'qualifications1', 'recognition1', 'subscription1', 'contradiction1', 'modification1', 'transmission1', 'manufacturing1', 'configuration1', 'specialities1', 'appreciation1', 'authentication1', 'collaboration1', 'communication1', 'demonstration1', 'documentation1', 'experimentation1', 'identification1', 'implementation1', 'intervention1', 'justification1', 'mathematician1', 'multiplication1', 'notification1', 'perspiration1', 'preoccupation1', 'rehabilitation1', 'representation1', 'restructuring1', 'satisfaction1', 'simplification1', 'specification1', 'stabilization1', 'standardization1', 'subordination1', 'substantiation1', 'transportation1', 'transvaluation1', 'verification1', 'visualization1', 'accommodation1', 'accountability1', 'appropriation1', 'centralization1', 'characterization1', 'confrontation1', 'congratulation1', 'decentralization1', 'determination1', 'differentiation1', 'digitalization1', 'diversification1', 'elaboration1', 'generalization1', 'harmonization1', 'instrumentation1', 'international1', 'misrepresentation1'
'explanation2', 'hypothesize2', 'combination2', 'personality2', 'calculation2', 'destination2', 'exploration2', 'architecture2', 'university2', 'consequence2', 'possibility2', 'organization2', 'considerable2', 'protectional2', 'environment2', 'transmission2', 'measurement2', 'presentation2', 'exaggeration2', 'concentration2', 'examination2', 'illustration2', 'optimization2', 'contribution2', 'determination2', 'announcement2', 'capabilities2', 'publication2', 'observation2', 'registration2', 'expectations2', 'introduction2', 'transparency2', 'arrangement2', 'exploitation2', 'installation2', 'preparation2', 'coordination2', 'manipulation2', 'participation2', 'qualifications2', 'recognition2', 'subscription2', 'contradiction2', 'modification2', 'transmission2', 'manufacturing2', 'configuration2', 'specialities2', 'appreciation2', 'authentication2', 'collaboration2', 'communication2', 'demonstration2', 'documentation2', 'experimentation2', 'identification2', 'implementation2', 'intervention2', 'justification2', 'mathematician2', 'multiplication2', 'notification2', 'perspiration2', 'preoccupation2', 'rehabilitation2', 'representation2', 'restructuring2', 'satisfaction2', 'simplification2', 'specification2', 'stabilization2', 'standardization2', 'subordination2', 'substantiation2', 'transportation2', 'transvaluation2', 'verification2', 'visualization2', 'accommodation2', 'accountability2', 'appropriation2', 'centralization2', 'characterization2', 'confrontation2', 'congratulation2', 'decentralization2', 'determination2', 'differentiation2', 'digitalization2', 'diversification2', 'elaboration2', 'generalization2', 'harmonization2', 'instrumentation2', 'international2', 'misrepresentation2'
'explanation3', 'hypothesize3', 'combination3', 'personality3', 'calculation3', 'destination3', 'exploration3', 'architecture3', 'university3', 'consequence3', 'possibility3', 'organization3', 'considerable3', 'protectional3', 'environment3', 'transmission3', 'measurement3', 'presentation3', 'exaggeration3', 'concentration3', 'examination3', 'illustration3', 'optimization3', 'contribution3', 'determination3', 'announcement3', 'capabilities3', 'publication3', 'observation3', 'registration3', 'expectations3', 'introduction3'
]

def domains():
    headers = {

        'Referer': 'https://mail.tm/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    }
    domain =[]
    domains= requests.get('https://api.mail.tm/domains', headers=headers).json()
    #domain= domains['hydra:member'][0]['domain']
    #print(domain)
    if 'hydra:member' in domains:
        domain= domains['hydra:member'][0]['domain']
    
        return domain
    else:
        print('looix')
        return None




def countdown(delay):
    for remaining_time in range(delay, -1, -1):
        colors = [
            "\033[1;37mH\033[1;36mo\033[1;35ma\033[1;32mn\033[1;31mg \033[1;34mH\033[1;33mu\033[1;36my\033[1;36m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;31mo\033[1;37ma\033[1;36mn\033[1;32mg \033[1;35mH\033[1;37mu\033[1;33my\033[1;32m🍉 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
            "\033[1;31mH\033[1;37mo\033[1;36ma\033[1;33mn\033[1;35mg \033[1;32mH\033[1;34mu\033[1;35my\033[1;37m🍉 - Tool\033[1;33m Vip \033[1;31m MIGATO\033[1;32m",
            "\033[1;32mH\033[1;33mo\033[1;34ma\033[1;35mn\033[1;36mg \033[1;37mH\033[1;36mu\033[1;31my\033[1;34m🍉 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
            "\033[1;37mH\033[1;34mo\033[1;35ma\033[1;36mn\033[1;32mg \033[1;33mH\033[1;31mu\033[1;37my\033[1;34m🍉 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
            "\033[1;34mH\033[1;33mo\033[1;37ma\033[1;35mn\033[1;31mg \033[1;36mH\033[1;36mu\033[1;32my\033[1;37m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
            "\033[1;36mH\033[1;35mo\033[1;31ma\033[1;34mn\033[1;37mg \033[1;35mH\033[1;32mu\033[1;36my\033[1;33m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            sleep(0.12)
    print("\r                          \r", end="")
    print("\033 THỜI GIAN CHỜ       ", end="\r")
#with open('useragent.txt', 'r') as file:
    #user_agents = file.readlines()

# Remove any leading/trailing whitespace (like \n) from each line
#user_agents = [agent.strip() for agent in user_agents]

# Select a random User-Agent
#random_user_agent = random.choice(user_agents)

def stard():
    global delay
    print('Đang Get Domains')
    Domains=domains()
    print(f'Đã gét Domain : {Domains}')
    delay=int(input('Delay Tạo Email :'))
    while True:
        countdown(delay)
        try:
            random_Domain = random.choice(Domain)
            random_word = random.choice(passw)
            random_number = random.randint(156, 168953)    
            DOMAINUSER=f'{random_Domain}{random_number}'
            PASSUSER=f'{random_word}{random_number}'
            headers = {
                'Referer': 'https://mail.tm/',
            }

            json_data = {
                'address': f'{DOMAINUSER}@{Domains}',
                'password': f'{PASSUSER}',
            }

            response = requests.post('https://api.mail.tm/accounts', headers=headers, json=json_data)
            #print(response.text)

            # Print the full JSON response


            # Parse the JSON response
            response_data = response.json()

            # Extract and print the 'id'
            if 'address'and'id' in response_data:
                print("--------------------------------------------------")
                print(f'{vang}Tạo tại khoản thàng công!!')
                print(f'{lam}ID:',response_data['id'])
                print(f'{lam}EMAIL',response_data['address'])
                print(f"{lam}TÀI KHOẢN:{DOMAINUSER}|{PASSUSER}")
                print("--------------------------------------------------")
                with open('email.txt', "a") as email:
                    email.write(f"{DOMAINUSER}@{Domains}|{PASSUSER}\n")
            else:
                print("ID not found in response.")
        except:
            print("loi")
stard()