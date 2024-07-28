import models.chatu_utka_model as chatu_utka_model
import models.dog_warrior2_model as dog_warrior2_model
import models.salute_bend_model as salute_bend_model
import models.updog_leg_model as updog_leg_model
import cv2
import os
import asyncio
from gtts import gTTS
from playsound import playsound
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=2)

async def print_and_speak(text):
    print(text)
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(executor, play_sound, text)

def play_sound(text):
    tts = gTTS(text=text, lang='en')
    tts.save("temp.mp3")
    playsound("temp.mp3")
    os.remove("temp.mp3")
# List of Ashtanga yoga poses in the first series
first_series_poses = [
    "Sun Salutation A",
    "Sun Salutation B",
    "Standing triangles",
    "Standings",
    "Seating",
    "Closing Sequence"
]

first_series_standing_triangle = [
    "Padangusthasana A",
    "Padangusthasana B",
    "Padahastasana A",
    "Padahastasana B",
    "Utthita Trikonasana A",
    "Utthita Trikonasana B",
    "Utthita Parsvakonasana A",
    "Utthita Parsvakonasana B",
    "Prasarita Padottanasana A",
    "Prasarita Padottanasana B",
    "Prasarita Padottanasana C",
    "Prasarita Padottanasana D",
    "Parsvottanasana"
]

first_series_standing = [
    "Utthita Hasta Padangusthasana A",
    "Utthita Hasta Padangusthasana B",
    "Utthita Hasta Padangusthasana C",
    "Ardha Baddha Padmottanasana",
    "Utkatasana",
    "Virabhadrasana A",
    "Virabhadrasana B"
]

first_series_seating = [
    "Dandasana",
    "Paschimottanasana A",
    "Paschimottanasana B",
    "Paschimottanasana C",
    "Purvottanasana",
    "Triang Mukha Ek Pada Paschimottanasana",
    "Janu Sirsasana A",
    "Janu Sirsasana B",
    "Marichyasana A",
    "Marichyasana C",
    "Navasana",
    "Bhujapidasana A"
]

first_series_closing_squence = [
    "Salamba Sarvangasana",
    "Halasana",
    "Karnapidasana",
    "Uttana Padasana",
    "Sirsasana A",
    "Savasana"
]

async def predict(model, pose):
    image_path = os.path.abspath('latest_frame.jpg')
    while True:
        prediction = model.predict_image(image_path)
        if (prediction) == pose:
            await print_and_speak(f"Model prediction: {prediction}")
            return
        await asyncio.sleep(0.5)

async def sun_salutation_A():
    await print_and_speak("Inhale to Urdhva Hastasana, Upward Salute")
    
    await predict(salute_bend_model, "salute")
    await print_and_speak("Exhale to Uttanasana, Standing Forward Bend")
    
    await predict(salute_bend_model, "bend")
    
    await print_and_speak("Inhale to Ardha Uttanasana, Halfway Lift")
    
    await print_and_speak("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    
    await predict(chatu_utka_model, "chatu")
    await print_and_speak("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    
    await predict(updog_leg_model, "updog")
    await print_and_speak("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    
    await predict(dog_warrior2_model, "dog")
    await breaths_5()
    await print_and_speak("Inhale to Ardha Uttanasana, Halfway Lift")
    
    await predict(salute_bend_model, "bend")
    await print_and_speak("Exhale to Uttanasana, Standing Forward Bend")
    
    await print_and_speak("Inhale to Urdhva Hastasana, Upward Salute")
    
    await predict(salute_bend_model, "salute")
    await print_and_speak("Exhale to Samasthiti, Equal Standing Pose")
    

async def sun_salutation_B():
    await print_and_speak("Inhale to Utkatasana, Chair Pose")
    
    await predict(chatu_utka_model, "utka")
    await print_and_speak("Exhale to Uttanasana, Standing Forward Bend")
    
    await predict(salute_bend_model, "bend")
    
    await print_and_speak("Inhale to Ardha Uttanasana, Halfway Lift")
    
    await print_and_speak("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    
    await predict(chatu_utka_model, "chatu")
    await print_and_speak("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    
    await predict(updog_leg_model, "updog")
    await print_and_speak("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    
    await predict(dog_warrior2_model, "dog")
    await print_and_speak("Inhale to Virabhadrasana I, Warrior I (right foot forward)")
    
    await predict(dog_warrior2_model, "warrior2")
    await print_and_speak("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    
    await predict(chatu_utka_model, "chatu")
    await print_and_speak("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    
    await predict(updog_leg_model, "updog")
    await print_and_speak("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    
    await predict(dog_warrior2_model, "dog")
    await print_and_speak("Inhale to Virabhadrasana I, Warrior I (left foot forward)")
    
    await predict(dog_warrior2_model, "warrior2")
    await print_and_speak("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    
    await predict(chatu_utka_model, "chatu")
    await print_and_speak("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    
    await predict(updog_leg_model, "updog")
    await print_and_speak("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    
    await predict(dog_warrior2_model, "dog")   
    await breaths_5()
    await print_and_speak("Inhale to Ardha Uttanasana, Halfway Lift")
    
    await predict(salute_bend_model, "bend")
    await print_and_speak("Exhale to Uttanasana, Standing Forward Bend")
    
    await print_and_speak("Inhale to Utkatasana, Chair Pose")
    
    await predict(chatu_utka_model, "utka")
    await print_and_speak("Exhale to Samasthiti, Equal Standing Pose")
    
    
def standings_1():
    print("Inhale to Padangusthasana A, Big Toe Pose")
    print("Exhale to Padangusthasana B, Big Toe Pose")
    breaths_5()
    print("Inhale to Padahastasana A, Hand Under Foot Pose")
    print("Exhale to Padahastasana B, Hand Under Foot Pose")
    breaths_5()
    print("Move to Samasthiti, Equal Standing Pose")
    print("Inhale to right foot backwords")
    print("Exhale to Utthita Trikonasana A, Extended Triangle Pose (right foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Utthita Trikonasana A, Extended Triangle Pose (left foot forward)")
    breaths_5()
    print("Move to Samasthiti, Equal Standing Pose")
    print("Inhale to right foot backwords")
    print("Exhale to Utthita Trikonasana B, Revolved Triangle Pose (right foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Utthita Trikonasana B, Revolved Triangle Pose (left foot forward)")
    breaths_5()
    print("Move to Samasthiti, Equal Standing Pose")
    print("Move right foot backwords")
    print("Inhale to Virabhadrasana B, Warrior II (right foot forward)")
    print("Exhale to Utthita Parsvakonasana A, Extended Side Angle Pose")
    breaths_5()
    print("Inhale to Virabhadrasana B, Warrior II (right foot forward)")
    print("Exhale to right leg straight")
    print("Inhale to Virabhadrasana B, Warrior II (left foot forward)")
    print("Exhale to Utthita Parsvakonasana A, Extended Side Angle Pose")
    breaths_5()
    print("Inhale to Virabhadrasana B, Warrior II (left foot forward)")
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale right foot backwords")
    print("Exhale to Utthita Parsvakonasana B, Revolved Side Angle Pose (right foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Utthita Parsvakonasana B, Revolved Side Angle Pose (left foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale right foot backwords")
    print("Exhale to Prasarita Padottanasana A, Wide-Legged Forward Bend A")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Prasarita Padottanasana B, Wide-Legged Forward Bend B")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Prasarita Padottanasana C, Wide-Legged Forward Bend C")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Prasarita Padottanasana C, Wide-Legged Forward Bend C")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale right foot backwords")
    print("Exhale to Parsvottanasana, Pyramid Pose (right foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Parsvottanasana, Pyramid Pose (left foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Samasthiti, Equal Standing Pose")
    
def standings_2():
    print("Inhale to Utthita Hasta Padangusthasana A, Extended Hand to Big Toe Pose A (right foot forward)")
    breaths_5()
    print("Inhale to Utthita Hasta Padangusthasana B, Extended Hand to Big Toe Pose B (right foot to the side)")
    breaths_5()
    print("Inhale to Utthita Hasta Padangusthasana C, Extended Hand to Big Toe Pose C (right foot forward)")
    breaths_5()
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale to Utthita Hasta Padangusthasana A, Extended Hand to Big Toe Pose A (left foot forward)")
    breaths_5()
    print("Inhale to Utthita Hasta Padangusthasana B, Extended Hand to Big Toe Pose B (left foot to the side)")
    breaths_5()
    print("Inhale to Utthita Hasta Padangusthasana C, Extended Hand to Big Toe Pose C (left foot forward)")
    breaths_5()
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale")
    print("Exhale to Ardha Baddha Padmottanasana, Half Bound Lotus Standing Forward Bend (right foot)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale")
    print("Exhale to Ardha Baddha Padmottanasana, Half Bound Lotus Standing Forward Bend (left foot)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Samasthiti, Equal Standing Pose")
    print("Inhale to Utkatasana, Chair Pose")
    breaths_5()
    print("Inhale to Virabhadrasana A, Warrior I (right foot forward)")
    breaths_5()
    print("Inhale to Virabhadrasana B, Warrior II (right foot forward)")
    breaths_5()
    print("Inhale to Virabhadrasana B, Warrior II (left foot forward)")
    breaths_5()
    print("Inhale to Virabhadrasana A, Warrior I (left foot forward)")
    breaths_5()
    print("Inhale to standing")
    print("Exhale to Samasthiti, Equal Standing Pose")
    
def vinyasa_to_seat():
    print("Inhale to Urdhva Hastasana, Upward Salute")
    print("Exhale to Uttanasana, Standing Forward Bend")
    print("Inhale to Ardha Uttanasana, Halfway Lift")
    print("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    print("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    print("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    print("Jump to Seating")
    
def seatings():
    print("Dandasana, Staff Pose")
    breaths_5()
    print("Inhale")
    print("Exhale to Paschimottanasana A, Seated Forward Bend A")
    breaths_5()
    print("Inhale half up")
    print("Exhale to straight back")
    print("Inhale")
    print("Exhale to Paschimottanasana B, Seated Forward Bend B")
    breaths_5()
    print("Inhale half up")
    print("Exhale to straight back")
    print("Inhale")
    print("Exhale to Paschimottanasana C, Seated Forward Bend C")
    breaths_5()
    print("Inhale half up")
    print("Exhale to straight back")
    print("Inhale")
    print("Exhale to Purvottanasana, Upward Plank Pose")
    breaths_5()
    print("Inhale to seating")
    half_vinyasa()
    print("Exhale to Triang Mukha Ek Pada Paschimottanasana, Three-Limbed Forward Bend (right foot bend)")
    breaths_5()
    print("Inhale to seating")
    print("Exhale to Triang Mukha Ek Pada Paschimottanasana, Three-Limbed Forward Bend (left foot bend)")
    breaths_5()
    print("Inhale to seating")
    half_vinyasa()
    print("Exhale to Janu Sirsasana A, Head-to-Knee Pose A (right foot bend)")
    breaths_5()
    print("Inhale to seating")
    print("Exhale to Janu Sirsasana B, Head-to-Knee Pose B (right foot bend)")
    breaths_5()
    print("Inhale to seating")
    half_vinyasa()
    print("Exhale to Janu Sirsasana A, Head-to-Knee Pose A (left foot bend)")
    breaths_5()
    print("Inhale to seating")
    print("Exhale to Janu Sirsasana B, Head-to-Knee Pose B (left foot bend)")
    breaths_5()
    print("Inhale to seating")
    half_vinyasa()
    print("Exhale to Marichyasana A, Pose Dedicated to the Sage Marichi A (right foot bend)")
    breaths_5()
    print("Inhale to seating")
    print("Exhale to Marichyasana C, Pose Dedicated to the Sage Marichi C (right foot bend)")
    breaths_5()
    print("Inhale to seating")
    half_vinyasa()
    print("Exhale to Marichyasana A, Pose Dedicated to the Sage Marichi A (left foot bend)")
    breaths_5()
    print("Inhale to seating")
    print("Exhale to Marichyasana C, Pose Dedicated to the Sage Marichi C (left foot bend)")
    breaths_5()
    print("Inhale to seating")
    half_vinyasa()
    for _ in range(3):
        print("Exhale to Navasana, Boat Pose")
        breaths_5()
        print("Inhale to seating")
    half_to_bhuja()
    print("Exhale to Bhujapidasana, Shoulder-Pressing Pose")
    breaths_5()
    print("Inhale to lying down")
    
def closing():
    print("Exhale to Salamba Sarvangasana, Shoulder Stand")
    for _ in range (2):
        breaths_5()
    print("Inhale")
    print("Exhale to Halasana, Plow Pose")
    breaths_5()
    print("Inhale")
    print("Exhale to Karnapidasana, Ear Pressure Pose")
    breaths_5()
    print("Inhale to lying down")
    print("Exhale to Uttana Padasana, Extended Fish Pose")
    breaths_5()
    print("Inhale to seating")
    print("Exhale to Sirsasana A, Headstand")
    for _ in range (2):
        breaths_5()
    print("Inhale to lying down")
    print("Exhale to Savasana, Corpse Pose")

def half_vinyasa():
    print("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    print("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    print("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    print("Inhale to seating")

def half_to_bhuja():
    print("Exhale to Chaturanga Dandasana, Four-Limbed Staff Pose")
    print("Inhale to Urdhva Mukha Svanasana, Upward-Facing Dog Pose")
    print("Exhale to Adho Mukha Svanasana, Downward-Facing Dog Pose")
    print("Inhale to legs next to toes")

async def breaths_5():
    for _ in range(5):
        await print_and_speak("Inhale")
        await asyncio.sleep(3)
        await print_and_speak("Exhale")
        await asyncio.sleep(3)
        
def get_pose_from_API():
    pass


async def capture_frame(interval, save_path):
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break

        # Save the frame as an image
        cv2.imwrite(save_path, frame)
        await asyncio.sleep(interval)
        
async def display_camera():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            break
        
        # Flip the frame horizontally to create a mirror effect
        mirrored_frame = cv2.flip(frame, 1)
        
        # Display the mirrored frame
        cv2.imshow('Yoga Instructor', mirrored_frame)
        
        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Yield control to allow other tasks to run
        await asyncio.sleep(0.01)

async def main_loop():
    for pose in first_series_poses:
        if pose == "Sun Salutation A":
            await print_and_speak("starting with Sun Salutation A")
            await asyncio.sleep(10)
            for _ in range(3):
                await sun_salutation_A()
        elif pose == "Sun Salutation B":
            print("moving on to Sun Salutation B, lets take a breath")
            await asyncio.sleep(10)
            print("Inhale")
            await asyncio.sleep(1)
            print("Exhale")
            await asyncio.sleep(1)
            for _ in range(3):
                await sun_salutation_B()
        elif pose == "Standing triangles":
            standings_1()
        elif pose == "Standings":
            standings_2()
            vinyasa_to_seat()
        elif pose == "Seating":
            seatings()
        elif pose == "Closing Sequence":
            closing()
    print("Finished!")
    

async def main():
    save_path = os.path.abspath('latest_frame.jpg')
    capture_task = asyncio.create_task(capture_frame(0.5, save_path))
    display_task = asyncio.create_task(display_camera())
    other_task = asyncio.create_task(main_loop())

    await asyncio.gather(capture_task, display_task, other_task)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
    else:
        try:
            asyncio.run(main())
        finally:
            cap.release()
            cv2.destroyAllWindows()

