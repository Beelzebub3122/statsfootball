from statsbombpy import sb
# show all competitions
sb.competitions()

# show unique competitions
print(sb.competitions().drop_duplicates(['country_name', 'competition_name']))