embed
<drac2>
martialDie = f"d{4+2*((MonkLevel>4)+(MonkLevel>9)+(MonkLevel>15))}"
enoughKi = True
args = argparse(&ARGS&)
c = combat()
targets = args.get('t')
combatants = []
damRoll = vroll('2'+martialDie).total
dam = str(damRoll)+"[force]"
if c:
  combatants = [c.get_combatant(x) for x in targets]
dc = 8 + proficiencyBonus + wisdomMod
if combatants:
  s=[x.save('dex') for x in combatants]
else:
  s = []
if s:
  saved=[x.total>=dc for x in s]
else:
  saved = None
if get_cc("Ki Points") > 0:
  mod_cc("Ki Points", -1)
  title = f"{name} unleashes their Astral Arms!"
  desc = f"{name} summons their Astral Arms into reality. Each creature of their choice that they can see within 10 feet of them must succeed on a **DC {dc}** Dexterity saving throw or take 2{martialDie} force damage.\n**Damage: ** 2{martialDie} ({damRoll}) + 0 = `{dam}`\n"
  output = f""
  for x in range(len(s)):
    if not saved[x]:
      output += f"**{combatants[x]}**\n**DEX Save:** {s[x]}; Failure!\n{combatants[x].damage(dam).damage}\n"
    elif saved[x]:
      output += f"**{combatants[x]}**\n**DEX Save:** {s[x]}; Success!\n**Damage:** `0`\n"
  if c:
    c.me.add_effect("Astral Arms", f"-attack '{max(wisdomMod, dexterityMod, strengthMod) + proficiencyBonus}|1d8+{max(wisdomMod, dexterityMod, strengthMod)}[force]|For 10 minutes, these spectral arms hover near your shoulders or surround your arms (your choice). You determine the arms\’ appearance, and they vanish early if you are incapacitated or die. While the spectral arms are present, you gain the following benefits:\n● You can use your Wisdom modifier in place of your Strength modifier when making Strength checks and Strength saving throws.\n● You can use the spectral arms to make unarmed strikes.\n● When you make an unarmed strike with the arms on your turn, your reach for it is 5 feet greater than normal.\n● The unarmed strikes you make with the arms can use your Wisdom modifier in place of your Strength or Dexterity modifier for the attack and damage rolls, and their damage type is force.'", 100)
else:
  enoughKi = False
  title = "Insufficient ki points."
  desc = "Take a short or long rest to restore ki."
  output = f""
output += f"\nKi Points: {get_cc('Ki Points')}/{get_cc_max('Ki Points')}"
return f'-f "{output}"'
</drac2>
-title "<title>"
-desc "<desc>"
-thumb <image>
