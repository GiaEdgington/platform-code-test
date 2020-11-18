def update_quality(awards):
    for award in awards:
        award_loss = 1
        if award.name == 'Blue Star':
            award_loss = 2

        if award.name != 'Blue First' and award.name != 'Blue Compare':
            if award.quality > 0:
                if award.name != 'Blue Distinction Plus':
                    award.quality -= award_loss #Normal decrease
        else:
            if award.quality < 50:
                award.quality += 1
                if award.name == 'Blue Compare':
                    if award.expires_in < 11:
                        if award.quality < 50:
                            award.quality += 1
                    if award.expires_in < 6:
                        if award.quality < 50:
                            award.quality += 1

        if award.name != 'Blue Distinction Plus':
            award.expires_in -= 1

        if award.expires_in < 0:
            if award.name != 'Blue First':
                if award.name != 'Blue Compare':
                    if award.quality > 0:
                        if award.name != 'Blue Distinction Plus':
                            award.quality -= award_loss #Normal decrease if expired
                else:
                    award.quality = award.quality - award.quality
            else:
                if award.quality < 50:
                    award.quality += 1

