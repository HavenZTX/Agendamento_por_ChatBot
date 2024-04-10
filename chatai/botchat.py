from nltk.chat.util import Chat, reflections

class AppointmentScheduler:
    def __init__(self):
        self.appointments = {}

    def schedule_appointment(self, date, time, subject, name):
        if date not in self.appointments:
            self.appointments[date] = {}
        if time not in self.appointments[date]:
            self.appointments[date][time] = {'subject': subject, 'name': name}
            return True
        else:
            return False

    def get_available_slots(self, date):
        if date in self.appointments:
            return [time for time in self.appointments[date] if not self.appointments[date][time]]
        else:
            return []

    def book_appointment(self, date, time, name):
        if date in self.appointments and time in self.appointments[date] and not self.appointments[date][time]:
            self.appointments[date][time]['name'] = name
            return True
        else:
            return False
        
    def print_report(self):
        print("\nRelatório de Agendamentos:")
        for date, timeslots in self.appointments.items():
            for time, details in timeslots.items():
                if details:
                    print(f"Data: {date} | Horário: {time} | Assunto: {details['subject']} | Nome: {details['name']}")
                else:
                    print(f"Data: {date} | Horário: {time} | Horário Disponível")


def main():
    scheduler = AppointmentScheduler()

    while True:
        print("\nBem-vindo ao sistema de agendamento de reuniões!")
        print("1. Agendar uma reunião")
        print("2. Verificar horários disponíveis")
        print("3. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            date = input("Digite a data (DD/MM/AAAA): ")
            time = input("Digite o horário (HH:MM): ")
            subject = input("Digite o assunto da reunião: ")
            name = input("Digite seu nome: ")

            if scheduler.schedule_appointment(date, time, subject, name):
                print("Reunião agendada com sucesso!")
            else:
                print("Desculpe, este horário já está ocupado.")

        elif choice == '2':
            date = input("Digite a data para verificar os horários disponíveis (DD/MM/AAAA): ")
            available_slots = scheduler.get_available_slots(date)
            if available_slots:
                print("Horários disponíveis para", date, ":", available_slots)
            else:
                print("Não há horários disponíveis para", date)

        elif choice == '3':
            print("Obrigado por usar o sistema de agendamento. Até mais!")
            scheduler.print_report()
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")



if __name__ == "__main__":
    main()
