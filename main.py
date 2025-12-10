import dns.resolver

def extract_domain(email):
    try:
        domain = email.strip().split('@')[1]

        if "." not in domain:

            return None

        return domain

    except IndexError:
        return None

def check_domain(domain):
    try:
        # Проверяем MX записи
        try:
            answers = dns.resolver.resolve(domain, 'MX')

            for rdata in answers:

                print(rdata.to_text())
            if answers:
                return "домен валиден"

        except (dns.resolver.NoAnswer, dns.resolver.NoNameservers):

            return "MX-записи отсутствуют или некорректны"

        # Если MX нет — проверяем, существует ли домен
        try:
            dns.resolver.resolve(domain, 'A')

            return "MX-записи отсутствуют или некорректны"

        except dns.resolver.NXDOMAIN:
            return "домен отсутствует"



    except Exception:
        return "домен отсутствует"

def main():
    print("Введите email-адреса построчно (пустая строка — завершить):")
    emails = []
    while True:
        line = input()
        if line.strip() == "":
            break
        emails.append(line.strip())

    print("\nРезультаты проверки:")
    for email in emails:
        domain = extract_domain(email)
        if not domain:
            print(f"{email}: некорректный формат email")
            continue
        status = check_domain(domain)
        print(f"{email}: {status}")

if __name__ == "__main__":
    main()