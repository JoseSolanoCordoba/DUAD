class Head():
	def __init__(self):
		self.label = "Head"
		pass

class Hand():
	def __init__(self):
		self.label = "Hand"
		pass
	
class Feet():
	def __init__(self):
		self.label = "Feet"
		pass
	
class Arm():
	def __init__(self, hand):
		self.label = "Arm"
		self.hand = hand

class Leg():
	def __init__(self, feet):
		self.label = "Leg"
		self.feet = feet
		
class Torso():
	def __init__(self, head, right_arm, left_arm):
		self.label = "Torso"
		self.head = head
		self.right_arm = right_arm
		self.left_arm = left_arm

class Human():
    def __init__(self, torso, right_leg, left_leg):
        self.torso = torso
        self.right_leg = right_leg
        self.left_leg = left_leg

head_1 = Head()
right_hand = Hand()
right_hand.label = "right hand"
left_hand = Hand()
left_hand.label = "left hand"

right_arm = Arm(right_hand)
right_arm.label = "right arm"
left_arm = Arm(left_hand)
left_arm.label = "left arm"

right_feet = Feet()
right_feet.label = "right feet"
left_feet = Feet()
left_feet.label = "left feet"

right_leg = Leg(right_feet)
right_leg.label = "right leg"
left_leg = Leg(left_feet)
left_leg.label = "left leg"

torso_1 = Torso(head_1, right_arm, left_arm)

human_1 = Human(torso_1, right_leg, left_leg)

print(f"Humanbeing is constructed of: {human_1.torso.label} with one {human_1.torso.right_arm.label}, with one {human_1.torso.left_arm.label}, with one {human_1.torso.head.label}, and with one {human_1.right_leg.label} and one {human_1.left_leg.label}\n")
print(f"In parallel right arm contains one {human_1.torso.right_arm.hand.label}, and left arm contains one {human_1.torso.left_arm.hand.label}\n")
print(f"Right leg contains one {human_1.right_leg.feet.label} and left leg contains one {human_1.left_leg.feet.label}")
