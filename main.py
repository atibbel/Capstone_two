import random

# Globals
ok = 0
fail = 0
warn = 0


class ScoutSystemCheck:

  def __init__(self):
    self.system_check = 0
    self.system_status = ""

  # These methods each get passed a random status as defined in system_information()
  def antenna_check(self):
    print(
      f"Checking antennas (L/R):\t\t   {self.systems_check(self.system_information())}"
    )

  def camera_check(self):
    print(
      f"Checking camera:\t\t           {self.systems_check(self.system_information())}"
    )

  def arm_check(self):
    print(
      f"Checking arms:\t\t               {self.systems_check(self.system_information())}"
    )

  def torso_check(self):
    print(
      f"Checking torso:\t\t               {self.systems_check(self.system_information())}"
    )

  def leg_check(self):
    print(
      f"Checking legs:\t\t               {self.systems_check(self.system_information())}"
    )

  def ai_link(self):
    print(
      f"Checking connection:\t\t       {self.systems_check(self.system_information())}"
    )

  # Print status and update globals based on parameter passed
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

  # Return random status. Chances: [OK] 65% | [WARN] 25% | [FAIL] 10%
  def system_information(self):
    self.system_check = random.randint(0, 100)

    if self.system_check <= 65:
      return 1
    elif self.system_check <= 90:
      return 2
    else:
      return 0


# Execution
scout = ScoutSystemCheck()
print("\n\nStarting up....")
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

print(f"\nChecks completed with: {ok} [OK]  {warn} [WARN]  {fail} [FAIL]")

if fail == 0:
  print("SCOUT IS OPERATIONAL.")
else:
  print("SCOUT CANNOT OPERATE. SHUTTING DOWN...")
