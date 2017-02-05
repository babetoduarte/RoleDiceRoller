from RoleDiceRoller.DiceBag import DiceBag

db = DiceBag()
db.add_die(4, 'd4')
print("Rolling 3d4:")
print(db.roll_dice(3, 4))

db.add_die(20, 'd20')
print("Rolling 4d20:")
print(db.roll_dice(4, 20))