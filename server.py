from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re
app = Flask(__name__)

# data comes from goodreads.com
current_id = 30

books = [
    {
        "id": 0,
        "title": "Six of Crows",
        "author": "Leigh Bardugo",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1459349344l/23437156.jpg",
        "description": "Ketterdam: a bustling hub of international trade where anything can be had for the right price—and no one knows that better than criminal prodigy Kaz Brekker. Kaz is offered a chance at a deadly heist that could make him rich beyond his wildest dreams. But he can’t pull it off alone. . . . Kaz’s crew is the only thing that might stand between the world and destruction—if they don’t kill each other first.",
        "rating": 4.46,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Still just as amazing the second time around.",
            "This book is fantastic.",
            "words can't describe how much i love these characters."
        ]
    },
    {
        "id": 1,
        "title": "The Raven Boys",
        "author": "Maggie Stiefvater",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1573508485l/17675462._SY475_.jpg",
        "description": "It is freezing in the churchyard, even before the dead arrive. For as long as she can remember, Blue has been warned that she will cause her true love to die. She never thought this would be a problem. But now, as her life becomes caught up in the strange and sinister world of the Raven Boys, she’s not so sure anymore.",
        "rating": 4.06,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "You know that feeling when a book is so perfect that you just want to shove it down everyone's throat?",
            "(Sweet Caroline voice) so good! so good! so good!",
            "no better way to spend Halloween than rereading this book"
        ]
    },
    {
        "id": 2,
        "title": "The Night Circus",
        "author": "Erin Morgenstern",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1387124618l/9361589.jpg",
        "description": "The circus arrives without warning. No announcements precede it. It is simply there, when yesterday it was not. Within the black-and-white striped canvas tents is an utterly unique experience full of breathtaking amazements. It is called Le Cirque des Rêves, and it is only open at night.",
        "rating": 4.04,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "romance",
                "mark_as_deleted": False
            },
            {
                "name": "historical fiction",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "If I could trade places with anyone in the world, it’d be with someone experiencing this book for the first time.",
            "The prose sparkles, and the story itself is a feat of magical acrobatics.",
            "I have quite honestly never had the pleasure of reading a more beautiful book."
        ]
    },
    {
        "id": 3,
        "title": "A Darker Shade of Magic",
        "author": "V.E. Schwab",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400322851l/22055262.jpg",
        "description": "Kell is one of the last Antari—magicians with a rare, coveted ability to travel between parallel Londons; Red, Grey, White, and, once upon a time, Black. Kell was raised in Arnes—Red London—and officially serves the Maresh Empire as an ambassador, traveling between the frequent bloody regime changes in White London and the court of George III in the dullest of Londons, the one without any magic left to see.",
        "rating": 4.09,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "V.E. Schwab does it again!",
            "So, in a startling turn of events, this book is even more insufferably perfect the second time round.",
            "I sort of flew through this book."
        ]
    },
    {
        "id": 4,
        "title": "Geek Love",
        "author": "Katherine Dunn",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1366699063l/13872.jpg",
        "description": "Geek Love is the story of the Binewskis, a carny family whose mater- and paterfamilias set out—with the help of amphetamine, arsenic, and radioisotopes—to breed their own exhibit of human oddities. There’s Arturo the Aquaboy, who has flippers for limbs and a megalomaniac ambition worthy of Genghis Khan . . . Iphy and Elly, the lissome Siamese twins . . . albino hunchback Oly, and the outwardly normal Chick, whose mysterious gifts make him the family’s most precious—and dangerous—asset.",
        "rating": 3.97,
        "genres": [
            {
                "name": "horror",
                "mark_as_deleted": False
            },
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "contemporary",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Geek Love has a handful of the most memorable characters you’ll ever find.",
            "Geek Love is an amazing book, audacious, moving, beautiful, substantive, creepy, upsetting, tragic and dark.",
            "I love weird characters and twisted plot lines, but this went so far that it made me very uncomfortable. And I love the book for that."
        ]
    },
    {
        "id": 5,
        "title": "Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch",
        "author": "Terry Pratchett and Neil Gaiman",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1392528568l/12067.jpg",
        "description": "‘Armageddon only happens once, you know. They don’t let you go around again until you get it right.’ People have been predicting the end of the world almost from its very beginning, so it’s only natural to be sceptical when a new date is set for Judgement Day. But what if, for once, the predictions are right, and the apocalypse really is due to arrive next Saturday, just after tea?",
        "rating": 4.25,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "humor",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "From the four bikers of the apocalypse to adorable hell hounds, it's my absolute favorite offering from Terry Pratchett -- his humor mixed with Neil Gaiman's is absolute win in my opinion.",
            "This is actually a profound philosophical and theological treatise, exploring good and evil, nature versus nurture, free will, war, pollution, and organised religion.",
            "Loved every second of it!"
        ]
    },
    {
        "id": 6,
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1559986152l/386162.jpg",
        "description": "Join Douglas Adams's hapless hero Arthur Dent as he travels the galaxy with his intrepid pal Ford Prefect, getting into horrible messes and generally wreaking hilarious havoc. Dent is grabbed from Earth moments before a cosmic construction team obliterates the planet to build a freeway. You'll never read funnier science fiction; Adams is a master of intelligent satire, barbed wit, and comedic dialogue. The Hitchhiker's Guide is rich in comedic detail and thought-provoking situations and stands up to multiple reads. Required reading for science fiction fans, this book (and its follow-ups) is also sure to please fans of Monty Python, Terry Pratchett's Discworld series, and British sitcoms.",
        "rating": 4.22,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "humor",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Another classic. If you don't like this series, you probably put your babel fish in the wrong hole.",
            "In my experience, readers either love Adams' books or quickly put them down.",
            "Douglas Adams' The Hitchhiker's Guide to the Galaxy is an entertaining romp through the galaxy."
        ]
    },
    {
        "id": 7,
        "title": "The Foxhole Court",
        "author": "Nora Sakavic",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1358594228l/17259690.jpg",
        "description": "Neil Josten is the newest addition to the Palmetto State University Exy team. He's short, he's fast, he's got a ton of potential—and he's the runaway son of the murderous crime lord known as The Butcher. Signing a contract with the PSU Foxes is the last thing a guy like Neil should do. The team is high profile and he doesn't need sports crews broadcasting pictures of his face around the nation.",
        "rating": 4.11,
        "genres": [
            {
                "name": "contemporary",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "The Foxhole Court was definitely a surprise, wherein I didn't get anything that I was expecting. However, I got a lot of which I didn't even know I needed.",
            "Danger, intensity, sports, addiction, illegal activity, reckless characters… You have it all.",
            "Let me introduce you to my most recent obsession."
        ]
    },
    {
        "id": 8,
        "title": "Carry On",
        "author": "Rainbow Rowell",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1481729252l/32768522.jpg",
        "description": "Simon Snow is the worst Chosen One who's ever been chosen.  Carry On - The Rise and Fall of Simon Snow is a ghost story, a love story and a mystery. It has just as much kissing and talking as you'd expect from a Rainbow Rowell story - but far, far more monsters.",
        "rating": 4.24,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            },
            {
                "name": "romance",
                "mark_as_deleted": False
            },
        ],
        "reviews": [
            "Hello 911 yes I just finished Carry On and I’d like to surgically remove my feelings",
            "New addition to my all time favorites list.",
            "Sorry, this book is just too meta for me, man."
        ]
    },
    {
        "id": 9,
        "title": "Aristotle and Dante Discover the Secrets of the Universe",
        "author": "Benjamin Alire Sáenz",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1328320260l/12000020.jpg",
        "description": "Aristotle is an angry teen with a brother in prison. Dante is a know-it-all who has an unusual way of looking at the world. When the two meet at the swimming pool, they seem to have nothing in common. But as the loners start spending time together, they discover that they share a special friendship—the kind that changes lives and lasts a lifetime.",
        "rating": 4.34,
        "genres": [
            {
                "name": "contemporary",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            },
            {
                "name": "romance",
                "mark_as_deleted": False
            },
        ],
        "reviews": [
            "This book was so so beautiful.",
            "I'M NOT CRYING YOU'RE CRYING",
            "I think I rarely read an introduction to a book that touched me as much as this one did."
        ]
    },
    {
        "id": 10,
        "title": "Strange the Dreamer",
        "author": "Laini Taylor",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1519915549l/28449207._SY475_.jpg",
        "description": "The dream chooses the dreamer, not the other way around—and Lazlo Strange, war orphan and junior librarian, has always feared that his dream chose poorly. Since he was five years old he’s been obsessed with the mythic lost city of Weep, but it would take someone bolder than he to cross half the world in search of it. Then a stunning opportunity presents itself, in the person of a hero called the Godslayer and a band of legendary warriors, and he has to seize his chance or lose his dream forever.",
        "rating": 4.32,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "romance",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Have you ever loved a book so much that it completely fills your soul, warms your heart, and heals your broken pieces?",
            "Ok but can you just give me a moment while I suffocate with the beauty and perfection that is this book.",
            "This book made me feel hopeful."
        ]
    },
    {
        "id": 11,
        "title": "Lizard Radio",
        "author": "Pat Schmatz",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1425907417l/24727102.jpg",
        "description": "Fifteen-year-old Kivali has never fit in. As a girl in boys’ clothes, she is accepted by neither tribe, bullied by both. What are you? they ask. Abandoned as a baby wrapped in a T-shirt with an image of a lizard on the front, Kivali found a home with nonconformist artist Sheila. Is it true what Sheila says, that Kivali was left by a mysterious race of saurians and that she’ll one day save the world?",
        "rating": 3.61,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "This book is weird as hell and I love it.",
            "Do you want to read a dystopian novel with a genderqueer protagonist who may or may not be part lizard?",
            "Lizard Radio is a lovely, messy, very queer book with queer characters."
        ]
    },
    {
        "id": 12,
        "title": "The Bear and the Nightingale",
        "author": "Katherine Arden",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1470731420l/25489134._SX318_.jpg",
        "description": "At the edge of the Russian wilderness, winter lasts most of the year and the snowdrifts grow taller than houses. But Vasilisa doesn't mind—she spends the winter nights huddled around the embers of a fire with her beloved siblings, listening to her nurse's fairy tales. Above all, she loves the chilling story of Frost, the blue-eyed winter demon, who appears in the frigid night to claim unwary souls. Wise Russians fear him, her nurse says, and honor the spirits of house and yard and forest that protect their homes from evil.",
        "rating": 4.12,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "historical fiction",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "This book is magical. This book is whimsical. This book is one of the best things I’ve read in my entire life.",
            "A beautiful, pastoral fairy tale set in a fantasy version of medieval Russia.",
            "Haunting. Riveting. Entrancing."
        ]
    },
    {
        "id": 13,
        "title": "The Giver",
        "author": "Lois Lowry",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1342493368l/3636.jpg",
        "description": "Through his wisdom and mannerism, Jonas is selected as the Receiver of Memory, a post that distinguishes him from others and gives him authority. He follows the rules and receives wisdom in the form of memories, but soon becomes upset with the rules. He is shocked at the killing of babies and others. Jonas, finally, wants to get rid of this society and saves the baby that is being released or killed by his father. The two go to Elsewhere to in search of freedom, hope, life and colors.",
        "rating": 4.13,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "dystopia",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "I've taught this book to my 6th graders nine years in a row. Once I realized that the book is actually a mystery, and not the bland sci-fi adventure it seemed at first skim, I loved it more and more each time.",
            "I don't remember reading a book as fast as I read this one.",
            "Man oh man, for a children's book...Lowry certainly didn't pull any punches."
        ]
    },
    {
        "id": 14,
        "title": "Flatland",
        "author": "Edwin Abott",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1512508446l/36949186._SY475_.jpg",
        "description": "This masterpiece of science (and mathematical) fiction is a delightfully unique and highly entertaining satire that has charmed readers for more than 100 years. The work of English clergyman, educator and Shakespearean scholar Edwin A. Abbott (1838-1926), it describes the journeys of A. Square [sic – ed.], a mathematician and resident of the two-dimensional Flatland, where women-thin, straight lines-are the lowliest of shapes, and where men may have any number of sides, depending on their social status. Through strange occurrences that bring him into contact with a host of geometric forms, Square has adventures in Spaceland (three dimensions), Lineland (one dimension) and Pointland (no dimensions) and ultimately entertains thoughts of visiting a land of four dimensions—a revolutionary idea for which he is returned to his two-dimensional world.",
        "rating": 4.09,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "satire",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "It is an absolutely brilliant work of speculative mathematics deftly hidden in a peculiar but strangely amusing social satire.",
            "Take a classically styled, 19th century satire about Victorian social mores…dress it up in dimensional geometry involving anthropomorphized shapes (e.g., lines, squares, cubes, etc.)…bathe it in the sweet, scented waters of social commentary…and wrap it all around humble, open-minded Square as protagonist.",
            "A curious little novella about a man a two-dimensional world thinking literally out of the box."
        ]
    },
    {
        "id": 15,
        "title": "Mrs. Caliban",
        "author": "Rachel Ingalls",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1488557112l/34377087.jpg",
        "description": "In the quiet suburbs, while Dorothy is doing chores and waiting for her husband to come home from work, not in the least anticipating romance, she hears a strange radio announcement about a monster who has just escaped from the Institute for Oceanographic Research… Reviewers have compared Rachel Ingalls’s Mrs. Caliban to King Kong, Edgar Allan Poe’s stories, the films of David Lynch, Beauty and the Beast, The Wizard of Oz, E.T., Richard Yates’s domestic realism, B-horror movies, and the fairy tales of Angela Carter—how such a short novel could contain all of these disparate elements is a testament to its startling and singular charm.",
        "rating": 3.81,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "magical realism",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "It's a slim book, probably more novella than novel, but I thoroughly enjoyed this quirky, weird, sweet book.",
            "Oh, wow. This is not your average human/monster romance. I totally understand why this landed on the BBMC’s top 20 American novels of the post-World War II period.",
            "If you like avocados you will like this book."
        ]
    },
    {
        "id": 16,
        "title": "The Left Hand of Darkness",
        "author": "Ursula K. Le Guin",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1488213612l/18423._SY475_.jpg",
        "description": "A groundbreaking work of science fiction, The Left Hand of Darkness tells the story of a lone human emissary to Winter, an alien world whose inhabitants can choose—and change—their gender. His goal is to facilitate Winter's inclusion in a growing intergalactic civilization. But to do so he must bridge the gulf between his own views and those of the completely dissimilar culture that he encounters. Embracing the aspects of psychology, society, and human emotion on an alien world, The Left Hand of Darkness stands as a landmark achievement in the annals of intellectual science fiction.",
        "rating": 4.07,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "What is underneath the labels - is it simply humanity?",
            "This book is quite astonishing.",
            "This was written in the sixties, though it feels like it was written yesterday."
        ]
    },
    {
        "id": 17,
        "title": "A Game of Thrones",
        "author": "George R.R. Martin",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1562726234l/13496.jpg",
        "description": "Long ago, in a time forgotten, a preternatural event threw the seasons out of balance. In a land where summers can last decades and winters a lifetime, trouble is brewing. The cold is returning, and in the frozen wastes to the north of Winterfell, sinister and supernatural forces are massing beyond the kingdom’s protective Wall. At the center of the conflict lie the Starks of Winterfell, a family as harsh and unyielding as the land they were born to. Sweeping from a land of brutal cold to a distant summertime kingdom of epicurean plenty, here is a tale of lords and ladies, soldiers and sorcerers, assassins and bastards, who come together in a time of grim omens.",
        "rating": 4.45,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Okay - I am SO incredibly late to this party but hey, I made it! And the hype was real!",
            "I thank the gods and the kings for making me read this.",
            "A shocking story that breaks fantasy conventions, it's seven hundred pages of realpolitik and character development."
        ]
    },
    {
        "id": 18,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1474154022l/3._SY475_.jpg",
        "description": "Harry Potter's life is miserable. His parents are dead and he's stuck with his heartless relatives, who force him to live in a tiny closet under the stairs. But his fortune changes when he receives a letter that tells him the truth about himself: he's a wizard. A mysterious visitor rescues him from his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry.",
        "rating": 4.47,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "adventure",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Simply put: not reading this book is voluntarily shutting yourself away from an incredible world of magic, myth, and entrancing mayhem.",
            "I can honestly say that I loved every minute of this.",
            "It's flipping magical (literally)!"
        ]
    },
    {
        "id": 19,
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1447303603l/2767052.jpg",
        "description": "In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV. Sixteen-year-old Katniss Everdeen, who lives alone with her mother and younger sister, regards it as a death sentence when she is forced to represent her district in the Games. But Katniss has been close to dead before - and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weigh survival against humanity and life against love.",
        "rating": 4.33,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "adventure",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "The Most Dangerous Game meets Survivor.",
            "A sharp and intelligent heroine with just the right amount of emotion who gives in to absolutely nothing and no one.",
            "The literal corruption of youth by reality television. Forced into murder, thievery, treachery, and kissing to stay alive."
        ]
    },
    {
        "id": 20,
        "title": "1984",
        "author": "George Orwell",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532714506l/40961427._SX318_.jpg",
        "description": "Among the seminal texts of the 20th century, Nineteen Eighty-Four is a rare work that grows more haunting as its futuristic purgatory becomes more real. Published in 1949, the book offers political satirist George Orwell's nightmarish vision of a totalitarian, bureaucratic world and one poor stiff's attempt to find individuality. The brilliance of the novel is Orwell's prescience of modern life—the ubiquity of television, the distortion of the language—and his ability to construct such a thorough version of hell. Required reading for students since it was published, it ranks among the most terrifying novels ever written.",
        "rating": 4.18,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "politics",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Gosh, probably the most haunting not to mention frightening book I've ever read.",
            "1984 is not a particularly good novel, but it is a very good essay.",
            "I got the chills so many times toward the end of this book. It completely blew my mind."
        ]
    },
    {
        "id": 21,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1398034300l/5107.jpg",
        "description": "The hero-narrator of The Catcher in the Rye is an ancient child of sixteen, a native New Yorker named Holden Caulfield. Through circumstances that tend to preclude adult, secondhand description, he leaves his prep school in Pennsylvania and goes underground in New York City for three days. The boy himself is at once too simple and too complex for us to make any final comment about him or his story. Perhaps the safest thing we can say about Holden is that he was born in the world not just strongly attracted to beauty but, almost, hopelessly impaled on it.",
        "rating": 3.80,
        "genres": [
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "coming of age",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "I read the end of The Catcher in the Rye the other day and found myself wanting to take Holden Caulfield by the collar and shake him really, really hard and shout at him to grow up.",
            "I LOVE IT when I go into a book with low expectations and it ends up knocking me on my ass.",
            "Holden is the teenage mind in all its confusion, rebellion and irrationality, and in all its undefined hope for individual heroism."
        ]
    },
    {
        "id": 22,
        "title": "All the Crooked Saints",
        "author": "Maggie Stiefvater",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1500451773l/30025336._SY475_.jpg",
        "description": "Any visitor to Bicho Raro, Colorado is likely to find a landscape of dark saints, forbidden love, scientific dreams, miracle-mad owls, estranged affections, one or two orphans, and a sky full of watchful desert stars. At the heart of this place you will find the Soria family, who all have the ability to perform unusual miracles. And at the heart of this family are three cousins longing to change its future: Beatriz, the girl without feelings, who wants only to be free to examine her thoughts; Daniel, the Saint of Bicho Raro, who performs miracles for everyone but himself; and Joaquin, who spends his nights running a renegade radio station under the name Diablo Diablo.",
        "rating": 3.84,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "magical realism",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "This book has owls and rock n' roll in it.",
            "I had to pause a couple times and reread certain passages. It was just so beautiful.",
            "This book can be summed up in a single word: magical."
        ]
    },
    {
        "id": 23,
        "title": "The Coldest Girl in Coldtown",
        "author": "Holly Black",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1367312471l/12813630.jpg",
        "description": "Tana lives in a world where walled cities called Coldtowns exist. In them, quarantined monsters and humans mingle in a decadently bloody mix of predator and prey. The only problem is, once you pass through Coldtown's gates, you can never leave. One morning, after a perfectly ordinary party, Tana wakes up surrounded by corpses. The only other survivors of this massacre are her exasperatingly endearing ex-boyfriend, infected and on the edge, and a mysterious boy burdened with a terrible secret. Shaken and determined, Tana enters a race against the clock to save the three of them the only way she knows how: by going straight to the wicked, opulent heart of Coldtown itself.",
        "rating": 3.85,
        "genres": [
            {
                "name": "paranormal",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Coldest Girl in Coldtown is not only unique, it's a fun, exciting story full of horror and blood with a little flair of post apocalyptic.",
            "Straight up brilliance!",
            " The Coldest Girl in Coldtown was a deliciously creepy and dark story, one that made my heart race and thrill."
        ]
    },
    {
        "id": 24,
        "title": "The Forest of Hands and Teeth",
        "author": "Carrie Ryan",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1320633297l/3432478.jpg",
        "description": "In Mary's world there are simple truths. The Sisterhood always knows best. The Guardians will protect and serve. The Unconsecrated will never relent. And you must always mind the fence that surrounds the village; the fence that protects the village from the Forest of Hands and Teeth. But, slowly, Mary’s truths are failing her. She’s learning things she never wanted to know about the Sisterhood and its secrets, and the Guardians and their power, and about the Unconsecrated and their relentlessness. When the fence is breached and her world is thrown into chaos, she must choose between her village and her future—between the one she loves and the one who loves her. And she must face the truth about the Forest of Hands and Teeth. Could there be life outside a world surrounded by so much death?",
        "rating": 3.59,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "young adult",
                "mark_as_deleted": False
            },
            {
                "name": "horror",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "ohhh boy, this was dark and filled with death and zombies and i loved every minute of it",
            "I particularly enjoyed this novel. The writing was beautiful, it was one of the best written novels I’ve read in a while.",
            "I found Ryan's writing beautifully and painfully evocative, and the present tense lent an immediacy to the narration that really worked."
        ]
    },
    {
        "id": 25,
        "title": "Dune",
        "author": "Frank Herbert",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1555447414l/44767458.jpg",
        "description": "Set on the desert planet Arrakis, Dune is the story of the boy Paul Atreides, heir to a noble family tasked with ruling an inhospitable world where the only thing of value is the spice melange, a drug capable of extending life and enhancing consciousness. Coveted across the known universe, melange is a prize worth killing for... When House Atreides is betrayed, the destruction of Paul's family will set the boy on a journey toward a destiny greater than he could ever have imagined. And as he evolves into the mysterious man known as Muad'Dib, he will bring to fruition humankind's most ancient and unattainable dream.",
        "rating": 4.22,
        "genres": ["fantasy", "science fiction", "adventure"],
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "adventure",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Machiavellian intrigue, mythology, religion, politics, imperialism, environmentalism, the nature of power.",
            "Perfection. Easily the number one book I've ever read.",
            "This is a phenomenal classic of literature."
        ]
    },
    {
        "id": 26,
        "title": "Orlando",
        "author": "Virginia Woolf",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1443118010l/18839._SY475_.jpg",
        "description": "Virginia Woolf's Orlando 'The longest and most charming love letter in literature', playfully constructs the figure of Orlando as the fictional embodiment of Woolf's close friend and lover, Vita Sackville-West. Spanning three centuries, the novel opens as Orlando, a young nobleman in Elizabeth's England, awaits a visit from the Queen and traces his experience with first love as England under James I lies locked in the embrace of the Great Frost. At the midpoint of the novel, Orlando, now an ambassador in Constantinople, awakes to find that he is now a woman, and the novel indulges in farce and irony to consider the roles of women in the 18th and 19th centuries. As the novel ends in 1928, a year consonant with full suffrage for women. Orlando, now a wife and mother, stands poised at the brink of a future that holds new hope and promise for women.",
        "rating": 3.87,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "historical fiction",
                "mark_as_deleted": False
            },
            {
                "name": "lgbtq",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Orlando to me is a dream come true in literature.",
            "This is a brilliant comic performance until Woolf, before finishing, runs out of steam",
            "I knew for sure I wasn't expecting anything like 'To the Lighthouse' with Orlando, but what I didn't know is just how much sheer pleasure Orlando would end up giving me, as this went right beyond my expectations, the days reading it seemed invigorated somehow."
        ]
    },
    {
        "id": 27,
        "title": "The Way of Kings",
        "author": "Brandon Sanderson",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1388184640l/7235533.jpg",
        "description": "I long for the days before the Last Desolation. The age before the Heralds abandoned us and the Knights Radiant turned against us. A time when there was still magic in the world and honor in the hearts of men. The world became ours, and yet we lost it. Victory proved to be the greatest test of all. Or was that victory illusory? Did our enemies come to recognize that the harder they fought, the fiercer our resistance? Fire and hammer will forge steel into a weapon, but if you abandon your sword, it eventually rusts away.",
        "rating": 4.65,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "I'm running out of superlatives.",
            "Ok, so I actually cried during this book.",
            "Incredible, impressive or fantastic, all these words are an understatement to the quality this book holds. The Way of Kings is the beginning of a masterpiece series in epic fantasy."
        ]
    },
    {
        "id": 28,
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1498841231l/35031085.jpg",
        "description": "Mary Shelley began writing Frankenstein when she was only eighteen. At once a Gothic thriller, a passionate romance, and a cautionary tale about the dangers of science, Frankenstein tells the story of committed science student Victor Frankenstein. Obsessed with discovering the cause of generation and life and bestowing animation upon lifeless matter, Frankenstein assembles a human being from stolen body parts but; upon bringing it to life, he recoils in horror at the creature's hideousness. Tormented by isolation and loneliness, the once-innocent creature turns to evil and unleashes a campaign of murderous revenge against his creator, Frankenstein.",
        "rating": 3.80,
        "genres": [
            {
                "name": "science fiction",
                "mark_as_deleted": False
            },
            {
                "name": "horror",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "Mary Shelley…I love you!!",
            "The worst thing about this novel is how distorted it has become by constant movie adaptations and misinformed ideas about the nature of Frankenstein and his monster.",
            "It's been fifty years since I had read Frankenstein, and, now—after a recent second reading—I am pleased to know that the pleasures of that first reading have been revived."
        ]
    },
    {
        "id": 29,
        "title": "Vicious",
        "author": "V.E. Schwab",
        "cover": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1532011194l/40874032._SY475_.jpg",
        "description": "Victor and Eli started out as college roommates—brilliant, arrogant, lonely boys who recognized the same sharpness and ambition in each other. In their senior year, a shared research interest in adrenaline, near-death experiences, and seemingly supernatural events reveals an intriguing possibility: that under the right conditions, someone could develop extraordinary abilities. But when their thesis moves from the academic to the experimental, things go horribly wrong. en years later, Victor breaks out of prison, determined to catch up to his old friend (now foe), aided by a young girl whose reserved nature obscures a stunning ability.",
        "rating": 4.24,
        "genres": [
            {
                "name": "fantasy",
                "mark_as_deleted": False
            },
            {
                "name": "science fiction",
                "mark_as_deleted": False
            }
        ],
        "reviews": [
            "I have so much of this book in my heart even my body feels too heavy to carry it.",
            "I absolutely loved Vicious, it kept me hooked right from the get-go and as things got more and more intense, I could not put it down!",
            "This is a book that explores the hero / villain dichotomy and promptly shatters it to pieces."
        ]
    }
]

# routes

@app.route('/')
def index():
   return render_template('index.html', books=books)

@app.route('/view/<ID>')
def view(ID=None):
    iden = int(ID)
    return render_template('view.html', books=books, iden=iden, title=books[iden]["title"], author=books[iden]["author"], cover=books[iden]["cover"], description=books[iden]["description"], rating=books[iden]["rating"], genres=books[iden]["genres"], reviews=books[iden]["reviews"])

@app.route('/create')
def create():
    return render_template('create.html', books=books)

@app.route('/search', methods=['GET', 'POST'])
def search():
    q = request.args.get('q')
    results = []
    for book in books:
        n_book = dict(book)
        if q.lower() in n_book["title"].lower():
            res = [i.start() for i in re.finditer(q.lower(), n_book["title"].lower())]
            res.reverse()
            for item in res:
                start = item
                print("start "+str(start))
                end = start + len(q)
                print("end "+str(end))
                n_book["title"] = n_book["title"][:start] + "<span class='highlight'>" + n_book["title"][start:end] + "</span>" + n_book["title"][end:]
                print(n_book["title"])
            results.append(n_book)
        if q.lower() in n_book["author"].lower():
            res = [i.start() for i in re.finditer(q.lower(), n_book["author"].lower())]
            res.reverse()
            for item in res:
                start = item
                print("start "+str(start))
                end = start + len(q)
                print("end "+str(end))
                n_book["author"] = n_book["author"][:start] + "<span class='highlight'>" + n_book["author"][start:end] + "</span>" + n_book["author"][end:]
                print(n_book["author"])
            if (n_book not in results):
                results.append(n_book)

    return render_template('search.html', books=results, title=q)


@app.route('/create_title', methods=['GET', 'POST'])
def create_title():
    global books
    global current_id

    json_data = request.get_json()   
    title = json_data["title"]
    author = json_data["author"]
    cover = json_data["cover"]
    description = json_data["description"]
    rating = json_data["rating"]
    genre1 = json_data["genre1"]
    print("genre1 "+genre1)
    genre2 = json_data["genre2"]
    print("genre2 "+genre2)
    genre3 = json_data["genre3"]
    print("genre3 "+genre3)
    review1 = json_data["review1"]
    review2 = json_data["review2"]
    review3 = json_data["review3"]

    book = {
        "id": current_id,
        "title": title,
        "author": author,
        "cover": cover,
        "description": description,
        "rating": rating,
        "genres": [
            {
                "name": genre1,
                "mark_as_deleted": False
            },
            {
                "name": genre2,
                "mark_as_deleted": False
            },
            {
                "name": genre3,
                "mark_as_deleted": False
            }
        ],
        "reviews": [review1, review2, review3]
    }

    print(book["genres"][0], book["genres"][1], book["genres"][2])

    current_id += 1

    books.append(book)

    return jsonify(id_ = book["id"])


@app.route('/edit_review', methods=['GET', 'POST'])
def edit_review():

    global books

    json_data = request.get_json()  
    iden = int( json_data["ID"] )
    review = json_data["review"]

    books[iden]["reviews"].append(review)

    return jsonify(review = review)

@app.route('/edit_rating', methods=['GET', 'POST'])
def edit_rating():

    global books

    json_data = request.get_json()  
    iden = int( json_data["ID"] )
    rating = json_data["rating"]

    books[iden]["rating"] = rating

    return jsonify(rating = rating)

@app.route('/delete_genre', methods=['GET', 'POST'])
def delete_genre():

    global books

    json_data = request.get_json()   
    book_id = int( json_data["book_id"] )
    genre_id = int( json_data["genre_id"] ) - 1
    
    # delete entry associated with id from array

    books[book_id]["genres"][genre_id]["mark_as_deleted"] = True

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(genres = books[book_id]["genres"])

@app.route('/undo_delete_genre', methods=['GET', 'POST'])
def undo_delete_genre():

    global books

    json_data = request.get_json()   
    book_id = int( json_data["book_id"] )
    genre_id = int( json_data["genre_id"] ) - 1
    
    # delete entry associated with id from array

    books[book_id]["genres"][genre_id]["mark_as_deleted"] = False

    #send back the WHOLE array of data, so the client can redisplay it
    return jsonify(genres = books[book_id]["genres"])

if __name__ == '__main__':
   app.run(debug = True)


# variables