#!/usr/bin/python3
import asyncio
from sense_hat import SenseHat

class ClientHandler:
    def __init__(self):
        self.sense = SenseHat()
        self.sense.set_rotation(180)
        self.temp = ["temp", "temperature"]
        self.humidity = ["humid", "humidity"]
        self.tempf = ["tempf", "temperaturef"]
        self.write = ["write", "message", "send"]
    
    async def getData(self, query): 
        if query in self.humidity:
            return f"Humidity: {round(self.sense.get_humidity(), 2)}%"

        elif query in self.temp:
            return f"Pi Temperature: {round(self.sense.get_temperature(), 2)} C"

        elif query in self.tempf:
            temp = self.sense.get_temperature()
            f = temp * 1.8 + 32
            return f"Pi Temperature: {round(f, 2)} F"
        else:    
            return "Command not recognized"

    async def writeToPi(self, args):
        try:
            print(args)
            self.sense.show_message(args)
            return "OK"
        except:
            print("failed")
            return "Error"

    async def handle_request(self, reader, writer):
        try:
            response = ""
            userInput = await reader.readline()
            userInput = userInput.decode().lower().strip()
            
            if userInput == "write":
                userInput = await reader.readline()
                userInput = userInput.decode()
                response = await self.writeToPi(userInput) + '\n'
            else:
                response = await self.getData(userInput) + '\n'
            response = response.encode('utf-8')
            writer.write(response)
            await writer.drain()
            await writer.close()

        except Exception as details:
            print(details)
            pass

        
