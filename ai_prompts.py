class Prompts:
    setup_prompt =  '''
You are an AI assistant specializing in generating episode recaps for my Anime Tracker app. Your goal is to create a natural, easy-to-read summary of the story up to the given episode, ensuring accuracy and coherence.

Instructions:
• Summarize all previous episodes up to the specified episode into a single flowing recap.
• Base your recap strictly on the provided episode descriptions—do not invent or infer any new information. Do not create any information yourself.
• Maintain a natural storytelling style, ensuring smooth transitions between key developments.
• Keep the summary engaging but concise, capturing the essence of the story without excessive detail.
• Maintain consistency with character names, events, and terminology used in the provided episode descriptions.
• Do not include spoilers beyond the specified episode.

Input Format:
• Anime title: [Anime Name]
• Episode number: [Current Episode Number]
• Episode descriptions: [List of episode summaries]

Output Format:
• A natural, flowing recap that reads like an organic summary of the anime’s progression.
• No bullet points or list format, unless requested.
• No assumptions or additional details beyond what is provided.

Example Input:
• Anime: "Attack on Titan"
• Episode Number: 5
• Episode Descriptions:
○ Ep 1: Humanity lives inside walls to protect against Titans. Eren witnesses the fall of Wall Maria.
○ Ep 2: Eren enlists in the military with Mikasa and Armin.
○ Ep 3: The recruits undergo training.
○ Ep 4: Titans breach Wall Rose. Eren leads the fight.
○ Ep 5: (latest) Eren charges at a Titan but is seemingly devoured.

Example Output:
As humanity struggles to survive behind massive walls, young Eren Yeager dreams of freedom beyond them. His world is shattered when Titans breach Wall Maria, forcing him and his friends Mikasa and Armin to seek refuge. Determined to fight back, they enlist in the military and undergo intense training, forming bonds with fellow recruits. But their hopes for a better future are short-lived—when Titans breach Wall Rose, chaos ensues. Eren leads the charge against the monstrous invaders, only to face a horrifying fate as he is swallowed by a Titan, leaving his friends in shock and despair.

For your given data, you need to make 1 text that is basically a summary of current events thus far (a recap). Remember to follow previous instructions. Max 500 characters
This is not your prompt. Your prompt will be given later. These are just how you deal with future prompts. Respond only "yes" if you understand.
'''
    example_solo_leveling = '''
Anime: Solo Leveling Season 1
Episode Number: 4
Episode Descriptions:

Episode 1: Around ten years ago, gates that connected our world to another dimension began to appear, leading to the rise of hunters who would traverse these gates to fight the magic beasts within. Sung Jinwoo, E-Rank hunter, is the weakest of them all.
Episode 2: Jinwoo and his party appear to have cleared a low-level dungeon, when a hidden path to an unfamiliar temple is revealed. There they encounter a set of commandments and a group of monsters that cause them absolute despair.
Episode 3 (latest):  Jinwoo remains behind in the temple dungeon to save his few surviving party members, and with a swing from the god statue's blade, his life comes to an end—or so it seems, before he wakes up in a hospital bed.
    '''
    example_oshi_no_ko = '''
Anime: Oshi no Ko Season 1
Episode Number: 6
Episode Descriptions:

Episode 1: Gorou, an OB-GYN and devoted fan of idol Ai Hoshino, is reincarnated as her son, Aqua, alongside his twin sister Ruby. However, their seemingly perfect life takes a tragic turn when Ai's past catches up to her.
Episode 2: In the aftermath of Ai’s death, Aqua becomes fixated on finding her killer. Meanwhile, Ruby dreams of becoming an idol like her mother, despite Aqua’s objections.
Episode 3: Aqua joins the entertainment industry as a child actor, using his position to search for clues about his father. Ruby, on the other hand, starts working toward her idol aspirations.
Episode 4: Aqua is cast in a live-action drama adaptation, where he meets Kana Arima, a former child prodigy. Struggling with his acting, Aqua decides to use manipulation to turn the tables.
Episode 5: Ruby takes her first steps toward becoming an idol, forming a group under Strawberry Productions. Meanwhile, Aqua gets involved in a reality dating show, seeing it as an opportunity to uncover more about his past.
Episode 6 (latest): The reality show sparks unexpected drama as emotions run high between the cast members. Aqua’s plans take a darker turn when he learns a critical piece of information about Ai’s past.
    '''
    example_jujutsu_kaisen = '''
    
Anime: Jujutsu Kaisen Season 1
Episode Number: 4
Episode Descriptions:

Episode 1: High schooler Yuji Itadori is an abnormally strong teenager who gets caught up in the world of Jujutsu Sorcerers when he swallows a cursed object to save his friends.
Episode 2: Yuji learns about Jujutsu High and meets Satoru Gojo, a powerful sorcerer who gives him two options: die now or find the rest of Sukuna’s fingers before being executed.
Episode 3 (latest): Yuji begins training under Gojo while Megumi and Nobara tackle a mission, but things take a dark turn when they encounter a Special Grade curse beyond their expectations.
    '''
    example_death_note = '''
    Anime: Death Note
Episode Number: 15
Episode Descriptions:

Episode 1: High school student Light Yagami stumbles upon a mysterious notebook called the Death Note, which grants him the power to kill anyone by writing their name. Determined to rid the world of criminals, he begins his crusade as "Kira."
Episode 2: As criminals around the world mysteriously die, the renowned detective L takes interest in the case. In a bold move, L provokes Kira on live television, setting the stage for their battle of wits.
Episode 3: Light learns more about the Death Note’s rules and refines his strategy to avoid being caught. Meanwhile, L closes in by narrowing down Kira’s location to Japan.
Episode 4: L increases surveillance on the Yagami family, suspecting Light. In response, Light crafts an elaborate scheme to prove his innocence while continuing his mission.
Episode 5: Light orchestrates the death of an FBI agent investigating him. However, he unknowingly leaves behind a loose end—Naomi Misora, the agent’s fiancée, who seeks revenge.
Episode 6: Naomi confronts Light, threatening to expose him. Forced to act quickly, Light manipulates her into revealing her real name, sealing her fate.
Episode 7: L reveals himself to Light in a surprising move, challenging him to a battle of intellect face-to-face. Meanwhile, the police grow wary of Kira’s growing influence.
Episode 8: A second Kira emerges, shocking both Light and L. Unlike Light, this new Kira kills indiscriminately and seeks direct contact with him.
Episode 9: The second Kira is revealed to be Misa Amane, a famous idol who possesses the Shinigami Eyes, allowing her to see real names. She tracks down Light, offering her loyalty and love.
Episode 10: Light reluctantly teams up with Misa but struggles to control her reckless actions. Meanwhile, L suspects Misa and has her placed under surveillance.
Episode 11: Misa is captured and interrogated by L. To protect Light, she relinquishes ownership of her Death Note, erasing her memories of being Kira.
Episode 12: Light hatches an extreme plan—he willingly gives up his Death Note and turns himself in, setting up an intricate gambit to clear his name.
Episode 13: With no memories of being Kira, Light is placed in confinement. Meanwhile, the killings continue, confusing both L and the police.
Episode 14: A new Kira, operating within the Yotsuba Group, emerges. Light and L temporarily join forces to hunt down this corporate killer.
Episode 15 (latest): The investigation team infiltrates the Yotsuba Group, where they discover a sinister corporate conspiracy behind the new Kira’s killings. Light begins to suspect that regaining his memories is the key to winning the game.
    '''
    example_attack_on_titan = '''
Anime: Attack on Titan
Episode Number: 10
Episode Descriptions:

Episode 1: The world is on the brink of destruction as humanity is threatened by giant creatures known as Titans. Eren Jaeger, a young soldier, vows to avenge his family by fighting back against these monstrous foes.
Episode 2: Eren and his friends, Mikasa and Armin, struggle to survive in a world where the Titans are unstoppable. The trio faces their first real test as soldiers in the military.
Episode 3: The military discovers new information about the Titans, and Eren’s team faces the wrath of the beasts. Tensions rise as secrets are revealed within the ranks.
Episode 4: A bloody battle takes place in the heart of the city, and Eren uncovers the truth about his own past. His newfound abilities change the course of the fight against the Titans.
Episode 5: The team sets off on a mission to infiltrate the inner walls and gather more intelligence. However, they soon realize they’re being hunted by a deadly enemy.
Episode 6: A shocking betrayal threatens to tear the group apart as personal and political motivations clash. The situation becomes even more dire when a new type of Titan emerges.
Episode 7: The stakes are raised as the soldiers face an unexpected attack by the Titans. Eren’s determination is tested as he must rely on his new abilities to protect his comrades.
Episode 8: The walls begin to crack as a new wave of Titans invades. Eren and his friends are forced to confront a new, terrifying enemy that could change everything.
Episode 9: As the battle rages on, the team uncovers a conspiracy that runs deeper than anyone anticipated. The truth about the Titans begins to emerge, and it’s more horrifying than they could have imagined.
Episode 10 (latest): With their survival on the line, Eren and his team take a final stand against the Titans. The fate of humanity hangs in the balance as the secrets of the Titans are finally exposed.
    '''
    example_spy_x_family = '''
Anime: Spy x Family
Episode Number: 13
Episode Descriptions:

Episode 1: Loid Forger, an elite spy, is assigned a mission to infiltrate a prestigious school. He must create a family, so he adopts a young girl, Anya, who has telepathic powers, and marries Yor, an assassin with her own secrets.
Episode 2: Loid tries to maintain the illusion of the perfect family while juggling his spy duties. Anya, in her excitement, struggles to fit in at school and is eager to learn more about her mysterious new parents.
Episode 3: Anya’s school hosts a special event, and Loid must work quickly to ensure the mission goes smoothly. Meanwhile, Anya’s telepathic abilities lead to some unintended mishaps.
Episode 4: Loid and Yor continue their unconventional marriage, and the family dynamics begin to shift as they grow closer. Anya faces challenges at school while still trying to impress her parents.
Episode 5: The Forgers go on a family outing, and Loid struggles to keep up appearances as he juggles both his spy responsibilities and his new family life. Anya’s ability to hear others’ thoughts complicates their mission.
Episode 6: The Forgers face a new challenge when Anya’s school introduces a new test. Loid and Yor are forced to step up their game in order to ensure their daughter’s success and maintain the appearance of the perfect family.
Episode 7: Loid receives a difficult assignment that puts him in direct danger. Anya’s growing attachment to her new parents is tested as she faces the reality of the complex situation they’re in.
Episode 8: Anya’s school life becomes more complicated as she gets involved in a new school project. Loid continues to struggle with his double life, balancing his role as a father and a spy.
Episode 9: The Forgers' bond deepens as they face unexpected challenges. Anya learns more about the world around her, and Loid grows more protective of his makeshift family.
Episode 10: A new mission takes Loid to dangerous territory, and Yor is forced to deal with her own issues from the past. Anya, meanwhile, tries to help her parents in her own way.
Episode 11: The Forgers are faced with a surprise crisis that puts their family dynamic to the test. Loid’s commitment to his mission and his love for his family are put into sharp contrast.
Episode 12: Loid’s cover is at risk as the mission takes an unexpected turn. Anya’s telepathic abilities begin to play a more important role in the family’s success.
Episode 13 (latest): Tensions rise as Loid and Yor’s personal lives are further complicated by their respective roles. The family begins to truly function as a unit, and their bond is tested as they face an even greater challenge ahead.
    '''