var adjs = [
    "beautiful",
    "great",
    "spectacular",
    "imaginative",
    "elegant",
    "awesome",
    "ambitious",
    "boundless",
    "brave",
    "bright",
    "charming",
    "cheerful",
    "comfortable",
    "confident",
    "courageous",
    "dashing",
    "dazzling",
    "delightful",
    "determined",
    "diligent",
    "eager",
    "efficient",
    "eminent",
    "enchanting",
    "encouraging",
    "energetic",
    "enthusiastic",
    "excellent",
    "excited",
    "exuberant",
    "fabulous",
    "fantastic",
    "fearless",
    "friendly",
    "funny",
    "generous",
    "glorious",
    "good",
    "industrious",
    "instinctive",
    "likeable",
    "lively",
    "lovely",
    "loving",
    "lucky",
    "perfect",
    "pleasant",
    "plucky",
    "productive",
    "resolute",
    "responsible",
    "righteous",
    "romantic",
    "seemly",
    "self-assured",
    "sensitive",
    "silly",
    "sincere",
    "skillful",
    "splendid",
    "successful",
    "talented",
    "thoughtful",
    "tough",
    "trustworthy",
    "upbeat",
    "vigorous",
    "vivacious",
    "warm",
    "wise",
    "witty",
    "wonderful",
    "respected",
    "cool"
]

var personal_nouns = [
    "hero",
    "adept",
    "achiever",
    "aficionado",
    "artist",
    "blessing",
    "celebrant",
    "champion",
    "dynamo",
    "dreamboat",
    "enthusiast",
    "enlightened",
    "genius",
    "go-getter",
    "spirit",
    "guru",
    "humanitarian",
    "icon",
    "idol",
    "individual",
    "innovator",
    "intellectual",
    "inventor",
    "leader",
    "optimist",
    "person",
    "human being",
    "soul",
    "philosopher",
    "philanthropist",
    "poet",
    "presence",
    "prodigy",
    "prophet",
    "sage",
    "saint",
    "scholar",
    "thinker",
    "specialist",
    "treasure",
    "visionary",
    "virtuoso",
    "wonder",
    "wunderkind",
    "youth",
];

var abstract_nouns = [
    "ability",
    "achievement",
    "acuity",
    "acumen",
    "admiration",
    "aesthetic",
    "affability",
    "affluence",
    "agelessness",
    "allure",
    "artistry",
    "avidity",
    "benevolence",
    "character",
    "clairvoyance",
    "clemency",
    "commitment",
    "competence",
    "compassion",
    "competence",
    "composure",
    "confidence",
    "congeniality",
    "consciousness",
    "courage",
    "credence",
    "charm",
    "curiosity",
    "dignity",
    "discipline",
    "distinction",
    "elegance",
    "eloquence",
    "eminence",
    "energy",
    "enthusiasm",
    "esteem",
    "excellence",
    "faith",
    "fearlessness",
    "fervor",
    "genorosity",
    "geniality",
    "goodness",
    "grace",
    "gravitas",
    "gumption",
    "harmony",
    "heroism",
    "importance",
    "independence",
    "individuality",
    "indomitability",
    "influence",
    "ingenuity",
    "initiative",
    "insight",
    "inspiration",
    "intellect",
    "joviality",
    "judgement",
    "kindness",
    "life",
    "love",
    "magnanimity",
    "magnificence",
    "majesty",
    "morale",
    "nobility",
    "opportunity",
    "optimism",
    "originality",
    "passion",
    "perception",
    "personality",
    "patience",
    "potential",
    "positivity",
    "power",
    "presence",
    "prestige",
    "prowess",
    "purpose",
    "quality",
    "radiance",
    "recognition",
    "resilience",
    "righteousness",
    "sensibility",
    "significance",
    "sincerity",
    "strength",
    "substance",
    "temperance",
    "understanding",
    "value",
    "virtue",
    "vision",
    "vitality",
    "warmth",
    "vibrancy",
    "wholeness",
    "wisdom",
    "wit",
    "worth",
];

function adj_compliment() {
    var adj = adjs[Math.floor(adjs.length*Math.random())];

    return "You are " + adj +"!";
}

function personal_noun_compliment() {
    var noun = personal_nouns[Math.floor(personal_nouns.length*Math.random())];

    if (Math.random() > .5) {
        if ((["a","e","i","o","u"]).indexOf(noun[0]) > 0) {
            noun = "an " + noun;
        } else {
            noun = "a " + noun;
        }
        return "You are " + noun + "!";
    } else {
        var adj = adjs[Math.floor(adjs.length*Math.random())];
        if ((["a","e","i","o","u"]).indexOf(adj[0]) > 0) {
            adj = "an " + adj;
        } else {
            adj = "a " + adj;
        }
        return "You are " + adj + " "+ noun + "!";
    }
}


function abstract_noun_compliment() {
    var noun = abstract_nouns[Math.floor(abstract_nouns.length*Math.random())];

    if (Math.random() > .5) {
        return "You have " + noun + "!";
    } else {
        var adj = adjs[Math.floor(adjs.length*Math.random())];
        return "You have " + adj + " "+ noun + "!";
    }
}


function compliment() {
    var funcs = [adj_compliment,personal_noun_compliment,abstract_noun_compliment];
    return funcs[Math.floor(funcs.length*Math.random())]();
}


