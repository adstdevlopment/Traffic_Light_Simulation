from statemachine import StateMachine, State


class TrafficLight(StateMachine):
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    cycle = green.to(yellow) | yellow.to(red) | red.to(green)

    def on_enter_green(self):
        print('Accelerate')

    def on_enter_yellow(self):
        print('Decelerate')

    def on_enter_red(self):
        print('Stop')
