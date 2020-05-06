from dzdp import DianpingComment

COOKIES = 'cy=3; cye=hangzhou; _lxsdk_cuid=16d640e3360c8-0596a57786c2ac-5b123211-1fa400-16d640e3360c8; _lxsdk=16d640e3360c8-0596a57786c2ac-5b123211-1fa400-16d640e3360c8; _hc.v=61f6c32c-b4ca-034b-7cfb-560857f6e19e.1569341715; s_ViewType=10; _dp.ac.v=9a0a5334-6038-4d5d-8467-31d2188b8c7b; dper=4aa8ec01edab87a96bef6fa0188303f04dbb1586f50a451245c351fecdf33d66387bcdf700e51478e05e42f150895ec2f726db6badfbd185ef64ff33954838faf69a9d5e3afe13a7c526b93c211055405b0b88a11f413b1463f48f0fe712940f; ua=dpuser_5306889493; ctu=87ef40fb04698d95ad55db24756553d956249ee29549931fd78a8a00470a6385; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=16dc5efce18-998-020-b33%7C%7C1'

class Custmer(DianpingComment):
    def _data_pipeline(self, data):
        print(data)
        with open('code_dict.txt','a+') as f:
            f.write(str(data) + '\n')
if __name__ == '__main__':
    dp = Custmer('67161528', cookies=COOKIES)
    dp.run()