import psycopg2


def findd(email):
    def postgr(csa):
        hostname = 'localhost'
        database = 'findfriends'
        username = 'postgres'
        pwd = 'root'
        port_id = 5432
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id
            )
            cur = conn.cursor()
            create_script = csa
            cur.execute(create_script)
            conn.commit()  # Commit the transaction before fetching results
            return cur.fetchall()
        except Exception as error:
            print(error)
        finally:
            if cur is not None:
                cur.close()

    def match_rate(*sets):
        intersection = set.intersection(*sets)
        union = set.union(*sets)
        if len(union) == 0:
            return 0
        else:
            return (len(intersection) / len(union)) * 100

    res = postgr('select * from findfri;')
    eml = postgr('''select "email" from friendfind;''')
    rec = [Username.strip() for Username, in eml]

    op=len(res)

    def latest(result,z,q,email):
        ax = {}
        ax[result[q][2].strip()] = []
        for i in range(0,z-1):
            if(i == q):
                continue
            else:
                a1=set(result[q][7])
                b1=set([result[i][7],result[i][8],result[i][9]])
                cr=match_rate(a1,b1)
                a2=set(result[q][8])
                cr+=match_rate(a2,b1)
                a3=set(result[q][9])
                cr+=match_rate(a3,b1)
                a = set(result[q][10:])
                b = set(result[i][10:])
                cr+=match_rate(a,b)
                ax[result[q][0].strip()].append((result[i][0].strip(), round(cr, 2)))
        for user, matches in ax.items():
            with open('./templates/FINDFRIENDS.txt','w') as f,open('./templates/FINDFRIENDS2.txt','w') as file:
                print(f"\n\n*Top 3 Matches for {user}:*")
                if not matches:
                    print("No matches found.")
                else:
                    sorted_matches = sorted(matches, key=lambda x: x[1], reverse=True)
                    for ix, match in enumerate(sorted_matches[:3], 1):
                        f.write(f"{match[0]} {match[1]}\n")
                        rin = postgr(f'''SELECT "email" FROM friendfind WHERE "name" = '{match[0]}';''')
                        if rin:
                            email = rin[0][0]
                            with open(f'match_{ix}.txt', 'w') as ma_file:
                                ma_file.write(email + '\n')
                        else:
                            print(f"No email found for {match[0]}")
                    highest_match_name = sorted_matches[0][0]
                    highest_match_rate = sorted_matches[0][1]
                    file.write(f"{highest_match_name}-{highest_match_rate}\n")
    if email in rec:
        qwer = rec.index(email)
        latest(res,op,qwer,email)
    else:
        print(f'{email} is not present in the list')

#ema= input("ENTER EMAIL")
#findd(ema)


