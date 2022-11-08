import random

ok = 0
fail = 0
warn = 0


class ScoutSystemCheck:

    def __init__(self):
        self.system_check = 0
        self.systems_good = True
        self.system_status = ""

    def antenna_check(self, system_check):
        if system_check == 0:
            self.system_status = "FAIL"
            global fail
            fail += 1
        elif system_check == 1:
            self.system_status = "OK"
            global ok
            ok += 1
        if system_check == 2:
            self.system_status = "WARN"
            global warn
            warn += 1

        print(f"Checking antennas (L/R):      [{self.system_status}]")

    def camera_check(self, system_check):
        if system_check == 0:
            self.system_status = "FAIL"
            global fail
            fail += 1
        elif system_check == 1:
            self.system_status = "OK"
            global ok
            ok += 1
        if system_check == 2:
            self.system_status = "WARN"
            global warn
            warn += 1
        print(f"Checking camera:              [{self.system_status}]")

    def arm_check(self, system_check):
        if system_check == 0:
            self.system_status = "FAIL"
            global fail
            fail += 1
        elif system_check == 1:
            self.system_status = "OK"
            global ok
            ok += 1
        if system_check == 2:
            self.system_status = "WARN"
            global warn
            warn += 1

        print(f"Checking arms:                [{self.system_status}]")

    def torso_check(self):
        self.system_check
        return self.system_check

    def leg_check(self):
        self.system_check = 1
        return self.system_check

    def ai_link(self):
        self.system_check = 1
        return self.system_check

    def all_systems_check(self):
        self.antenna_check()
        if self.leg_check():
            return 0

        if self.torso_check() and self.camera_check()\
                and self.camera_check() and self.ai_link():

            return self.all_systems_good


scout = ScoutSystemCheck()
print("\n\nStarting up ...")
print("FIRMWARE LOADED [OK]")
print("SOFTWARE LOADED [OK]")

print("\nBEGIN BOOT SEQUENCE CHECKS"
      "\n--------------------------")
scout.antenna_check(random.randint(0, 2))
scout.camera_check(random.randint(0, 2))
scout.arm_check(random.randint(0, 2))

print(f"\nChecks completed with {ok} [OK]  {warn} [WARN]  {fail} [FAIL]")


