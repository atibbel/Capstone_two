import random

ok = 0
fail = 0
warn = 0


class ScoutSystemCheck:

    def __init__(self):
        self.system_check = 0
        self.system_status = ""

    def antenna_check(self):
        print(f"Checking antennas (L/R):  {self.systems_check(self.system_information())}")

    def camera_check(self):
        print(f"Checking camera:          {self.systems_check(self.system_information())}")

    def arm_check(self):
        print(f"Checking arms:            {self.systems_check(self.system_information())}")

    def torso_check(self):
        print(f"Checking Torso:           {self.systems_check(self.system_information())}")

    def leg_check(self):
        print(f"Checking legs:            {self.systems_check(self.system_information())}")

    def ai_link(self):
        print(f"Checking connection:      {self.systems_check(self.system_information())}")

    def systems_check(self, system_check):
        if system_check == 0:
            self.system_status = "[FAIL] SCOUT cannot operate."
            global fail
            fail += 1
        elif system_check == 1:
            self.system_status = "[OK]"
            global ok
            ok += 1
        if system_check == 2:
            self.system_status = "[WARN] SCOUT service degraded. Repair or replace soon."
            global warn
            warn += 1

        return self.system_status

    def system_information(self):
        self.system_check = random.randint(0, 100)

        if self.system_check <= 65:
            return 1
        elif self.system_check <= 90 :
            return 2
        else:
            return 0


scout = ScoutSystemCheck()
print("\n\nStarting up ...")
print("FIRMWARE LOADED [OK]")
print("SOFTWARE LOADED [OK]")

print("\nBEGIN BOOT SEQUENCE CHECKS"
      "\n--------------------------")
scout.antenna_check()
scout.camera_check()
scout.arm_check()
scout.torso_check()
scout.leg_check()
scout.ai_link()

print(f"\nChecks completed with {ok} [OK]  {warn} [WARN]  {fail} [FAIL]")

if fail == 0:
    print("SCOUT IS OPERATIONAL")
else:
    print("SCOUT CANNOT OPERATE. SHUTTING DOWN...")





