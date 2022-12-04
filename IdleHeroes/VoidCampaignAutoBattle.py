import pyautogui
import time

# pyautogui.moveTo(100, 100, duration = 1)
# pyautogui.click(100, 100)

def actionSleep(func):
	def inner1():
		func()
		time.sleep(1)
	return inner1

@actionSleep
def defeatBattleClickConfirm():
	pyautogui.click(*DEFEAT_CONFIRM_POS)

@actionSleep
def clickBattle():
	pyautogui.click(*BATTLE_BUTTON_POS)

@actionSleep
def clickHeroDeploymentBattle():
	pyautogui.click(*HERO_DEPLOY_POS)

def isBattleOver():
	print(pyautogui.pixel(*DEFEAT_BANNER_COLOR_POS))
	return pyautogui.pixel(*DEFEAT_BANNER_COLOR_POS) == DEFEAT_BGCOLOR

def waitForBattleDefeat():
	while(not isBattleOver()):
		time.sleep(2)

def run():
	DELAY_START = 1
	print(f'Starting in {DELAY_START} sec')
	time.sleep(DELAY_START)
	for i in range(100):
		print(f'Loop: {i}')
		defeatBattleClickConfirm()
		clickBattle()
		clickHeroDeploymentBattle()
		waitForBattleDefeat()
		togglePositions()

def togglePositions():
	global BATTLE_BUTTON_POS, HERO_DEPLOY_POS, DEFEAT_CONFIRM_POS

	if BATTLE_BUTTON_POS == (3491, 1000):
		BATTLE_BUTTON_POS = HERO_DEPLOY_POS = DEFEAT_CONFIRM_POS = (3491, 1100)
	else:
		BATTLE_BUTTON_POS = HERO_DEPLOY_POS = DEFEAT_CONFIRM_POS = (3491, 1000)


MOUSE_POSITION_MODE = 0

# BATTLE_BUTTON_POS = (3242, 812)
# HERO_DEPLOY_POS = (3142, 812)
# DEFEAT_CONFIRM_POS = (3242, 812)
BATTLE_BUTTON_POS = HERO_DEPLOY_POS = DEFEAT_CONFIRM_POS = (3491, 1000)

DEFEAT_BANNER_COLOR_POS = (3443, 573)
DEFEAT_BGCOLOR = (15, 40, 81)

if MOUSE_POSITION_MODE:
	time.sleep(2)
	print(pyautogui.position())
	# pyautogui.displayMousePosition()

	px = pyautogui.pixel(3443, 573)
	print(f'COLOR: {px}')
else:
	run()