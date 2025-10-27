init python:

    def zona_reg_char(id, name, who_color, what_color="#fff", pref="", suf="", kind_mode="adv"):
        gl = globals()

        if kind_mode == "nvl":
            char_kind = nvl
        else:
            char_kind = adv

        gl[id] = Character(name, 
        color=who_color, what_color=what_color, 
        drop_shadow=[(2, 2)], drop_shadow_color="#000", what_drop_shadow=[(2, 2)], what_drop_shadow_color="#000",
        what_prefix=pref, what_suffix=suf,
        screen="zona_say",
        kind=char_kind,
        ctc=None, ctc_position="fixed"
        )

    zona_characters = [
        ("ptho", None, "#FFFFFF", "#ffffff", "«", "»"),
        ("vlad", "Влад", "#63748f"),
        ("kassa", "Кассирша", "#638f67"),
        ("hzkto", "Собеседник", "#FF0000"),
        ("proda", "Продавщица", "#e02b2b"),
        ("sotr1", "Сотрудник 1", "#323ee3"),
        ("sotr2", "Сотрудник 2", "#323ee3"),
        ("kiraark", "Кирилл Аркадьевич", "#56e041"),
        ("noname", "Незнакомец", "#56e041"),
        ("dicktofon", "Диктофон", "#a9aba9"),
        ("vanek", "Ванёк", "#858585"),
        ("igor", "Игорь", "#858585"),
        ("zmyself", "Я", "#858585"),         # ("im", "Я", "#858585"), <----- КАТЕГОРИЧЕСКИ НЕЛЬЗЯ ТАК!!
        ("ded", "Дед", "#858585"),
        ("babuska", "Бабушка", "#858585"),
        ("vois1", "Голос", "#00ea32"),
        ("pionka", "Пионерка", "#00ea32"),
        ("vojak", "Вожатая", "#00ea32"),
        ("vois2", "Голос", "#a5a5ff"),
        ("medsis", "Медсестра", "#a5a5ff"),
        ("vois3", "Голос", "#876fa3"),
        ("mira", "Мира", "#876fa3")
    ]

    def zona_set_nvl_mode():
        for char in zona_characters:
            zona_reg_char(*char, kind_mode="nvl")
        globals()['narrator'] = Character(
            None,
            kind=nvl,
            what_style="narrator_%s" % time_of_day,
            ctc=None,
            ctc_position="fixed"
        )

    def zona_set_adv_mode():
        for char in zona_characters:
            zona_reg_char(*char, kind_mode="adv")
        globals()['narrator'] = Character(
            None,
            kind=adv,
            what_style="narrator_%s" % time_of_day,
            ctc=None,
            ctc_position="fixed"
        )


