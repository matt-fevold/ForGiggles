from Classes import Character, World, Fight
from Classes.Units import Peasant
from Classes.Items.Armor.Head import Head

def conflict(character, char_list):
    # remove itself so no false positive
    char_list.remove(character)

    # print(len(char_list))

    for i in range(len(char_list)):
        if char_list[i].world_object.x_coord == character.world_object.x_coord:
            if char_list[i].world_object.y_coord == character.world_object.y_coord:
                return char_list[i]
    return False


def debugger():
    world.print_world()

    print()
    print()
    print("-" * world.width * 2)
    print()
    print()

    world.print_world_all_objects()

    print()
    print()

    print("-" * world.width)

world = World.World(6, 5)

character_list = []
Player = Character.Character(10, 1, "X", 3, 2, world, "Jim")
#Enemy_1 = Character.Character(5, 1, "Y", 0, 1, world, "Enemy_1")

character_list.append(Player)
#character_list.append(Enemy_1)

world.add_object(Player.world_object, Player.world_object.col, Player.world_object.row)
#world.add_object(Enemy_1.world_object, Enemy_1.world_object.col, Enemy_1.world_object.row)

#world.print_world()
#debugger()

peasant1 = Peasant.Peasant()
# peasant1.print_stats()
# x = Head.Head("asdf", 2)
# print(x)
peasant1.print_equipment()

# main game loop
gameover = True
while not gameover:
    world.print_world()
    print("(enter: 'right', 'left', 'up', 'down', 'quit')")
    move = str(input())

    if move in ["quit"]:
        gameover = True

    Player.walk(move)

    conflict_character = conflict(Player, character_list[:])
    if conflict_character is not False:

        fight = Fight.Fight(Player, conflict_character)
        while not fight.fight_over:
            fight.fight_screen()

            print("('attack', 'run')")
            action = str(input())

            # player action
            if action in ["attack", "run"]:


                if action in ["attack"]:
                    print("You attack for: " + str(fight.main_character.attack))
                    amount = fight.enemy_character.take_damage(fight.main_character.attack)

                    if fight.enemy_character.health <= 0:
                        fight.fight_over = True
                        world.remove_object(fight.enemy_character.world_object)
                        character_list.remove(fight.enemy_character)

                elif action in ["run"]:
                    fight.fight_over = True
                    Player.run(move)
                # enemy action
                print("Enemy attacks for: " + str())
            else:
                print("please enter valid move")


