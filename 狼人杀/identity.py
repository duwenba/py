
CAMP = {
    'GOOD':False,
    'BAD':True
}


class player(object):
    # information
    name: str
    job: str

    # flages
    kiled: bool
    voted_to_out: bool
    pass

class job(object):
    name:str
    camp:bool
    number:int
    def __init__(self,name,camp,number) -> None:
        self.name = name
        self.camp = camp
        self.number = number


preinstall_1= [
    job('villager',CAMP['GOOD'],3),
    job('werwolf',CAMP['BAD'],2),
    job('wizard',CAMP['GOOD'],1),
    job('SEER',CAMP['GOOD'],1),
]
