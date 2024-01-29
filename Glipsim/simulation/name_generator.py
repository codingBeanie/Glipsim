import random


class NameGenerator:
    def __init__(self):
        self.family_names = ["da", "wor", "wer", "wa", "er", "el", "ek", "em", "en",
                             "eb", "eas", "eor", "esa", "rou", "raf", "rill", "run",
                             "toh", "tom", "toff", "tlol", "tym", "zak", "zer", "ziu",
                             "zas", "um", "ung", "ulk", "ul", "urk", "ilo", "ig", "ima", "ila",
                             "ion", "iak", "olm", "of", "oka", "oki", "oba", "ob", "oq", "ok",
                             "pil", "pan", "par", "pen", "plo", "pa", "py", "paf", "pik",
                             "asa", "ask", "as", "al", "ak", "af", "am", "an", "ar", "at", "azo",
                             "sem", "sun", "sul", "sor", "sas", "sak", "saf", "sam", "san", "sar",
                             "dir", "dil", "dro", "dy", "dik", "do", "de", "dar", "dul", "deo",
                             "fro", "fi", "fan", "fre", "fyr", "fik", "fas", "fam", "for", "fu",
                             "glo", "gi", "gub", "gra", "ger", "gym", "gak", "gol", "gul", "gur",
                             "hik", "hom", "ha", "het", "hul", "her", "hyc", "han", "hep", "haf",
                             "jo", "jem", "jas", "jyl", "jip", "jar", "jor", "jul", "jek", "jaf",
                             "kal", "ko", "kem", "kyl", "kaf", "kam", "kum", "kun", "kak", "kaf",
                             "lof", "lam", "lan", "lers", "lil", "lul", "lur", "lak", "laf", "lavfs",
                             "ydri", "yda", "ylo", "yli", "can", "cak", "cik", "cok", "cuk", "cal", "caf",
                             "vol", "ver", "vava", "vun", "vle", "vik", "bre", "bar", "bun", "bik", "bif",
                             "blo", "bok", "buk", "bim", "nol", "nul", "nur", "nir", "nif", "naf", "nek", "nym",
                             "ma", "men", "myl", "maka", "muls"]
        self.child_names = ["ior", "yr", "yl", "yk", "ym",
                            "yf", "yria", "ylia", "ykia", "ymia", "yfia", "ytola"]

    def generate_family_name(self):
        sample = random.sample(self.family_names, 2)
        familyName = [sample[0].capitalize(), sample[1]]
        return (familyName)

    def generate_child_name(self, num):
        if num > 10:
            num = 10
        return (self.child_names[num])
