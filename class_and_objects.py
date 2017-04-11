lottery_plaer = {
'name':"Balram Pandey",
'number':(23,44,32,44)
}


class LotteryPlayer:
    name=""
    number=""
    def _init_(self):
        self.name = "Balram"
        self.number = (23,22,34,34)


player = LotteryPlayer()
print(player.name)
print(player.number)
