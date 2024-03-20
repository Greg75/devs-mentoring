participants = []
newcomers = int(input('How many new participants do you want to add: '))

for newcomer in range(newcomers):
    participant = input(f'Type newcomer number {newcomer + 1}: ')
    participants.append(participant)

for participant in participants:
    print(participant, end=' ')

participants.extend(['Adam', 'Ewa'])
participants.sort()
print(participants)
