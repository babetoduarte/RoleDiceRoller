from RoleDiceRoller.DiceBag import DiceBag
import hug

db = DiceBag()

@hug.get()
@hug.cli()
def roll(ndice):
    extra = 0
    info1 = ndice.split('d')
    amount = int(info1[0])
    if '+' in ndice:
        sides = int(info1[1].split('+')[0])
        extra = int(info1[1].split('+')[1])
    elif '-' in ndice:
        sides = int(info1[1].split('-')[0])
        extra = int(info1[1].split('-')[1])
        extra *= -1
    else:
        sides = int(info1[1])

    db.add_die(sides)
    roll_results = db.roll_dice(amount, sides)
    roll_sum = sum(roll_results)

    if extra > 0:
        print("Rolling "+str(amount)+"d"+str(sides) + "+" + str(extra) + ":")
        print(str(roll_results) + "+" + str(extra) + "=" + str(roll_sum + extra))
        return(str(roll_results) + "+" + str(extra) + "=" + str(roll_sum + extra))
    elif extra < 0:
        print("Rolling " + str(amount) + "d" + str(sides) + str(extra) + ":")
        print (str(roll_results) + str(extra) + "=" + str(roll_sum + extra))
        return(str(roll_results) + str(extra) + "=" + str(roll_sum + extra))
    else:
        print("Rolling " + str(amount) + "d" + str(sides) + ":")
        print(str(roll_results) + "=" + str(roll_sum))
        return(str(roll_results) + "=" + str(roll_sum))


if __name__ == '__main__':
    roll.interface.cli()

#roll('5d6')
#roll('2d20')
#roll('5d7+3')
#roll('3d8-2')
