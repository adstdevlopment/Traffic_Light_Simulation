from statemachine import StateMachine, State


class Vehicle(StateMachine):
    def __init__(self):
        move = State('Move')
        accelerate = State('Accelerate')
        decelerate = State('Decelerate')
        stop = State('Stop', initial=True)

        decelerate_speed = move.to(decelerate)
        accelerate_speed = stop.to(accelerate)
        stop_speed = decelerate.to(stop)
        move_speed = accelerate.to(move)

    def on_decelerate_speed(self):
        print("Deceleration")

    def on_accelerate_speed(self):
        print("Acceleration")

    def on_stop_speed(self):
        print("Stop")

    def on_move_speed(self):
        print("Move")

