from Classes.Actions import Action, MoveAction
from Classes.Actions.MoveAction import East, West, North, South, Camp
from Classes.Actions.MenuAction import Army, Inventory, Self


# returns a list of actions that every character should have
def basic_actions():

    # create list
    basic_action_list = []

    # movement actions
    east = East.East()
    west = West.West()
    north = North.North()
    south = South.South()
    basic_action_list.append(east)
    basic_action_list.append(west)
    basic_action_list.append(north)
    basic_action_list.append(south)

    camp = Camp.Camp()
    basic_action_list.append(camp)

    # menu actions
    view_army = Army.ViewArmy()
    basic_action_list.append(view_army)

    view_self = Self.ViewSelf()
    basic_action_list.append(view_self)

    edit_self = Self.EditSelf()
    basic_action_list.append(edit_self)

    # finish appending

    return basic_action_list

