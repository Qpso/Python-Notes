# just here to test random code
# yes it's supposed to be empty (usually)

physics_info = {
    "motion": {
        "definition": "Motion is the change in position of an object over time. It can be described using concepts like speed, velocity, and acceleration.",
        "formulas": ["speed = distance / time", "velocity = displacement / time", "acceleration = (final velocity - initial velocity) / time"],
        "additional_info": "Objects can be in motion even if they're not moving relative to a particular reference point. This is known as relative motion."
    },
    "forces": {
        "definition": "Forces are interactions between objects that cause them to change their motion. Some common types of forces include gravity, friction, and normal forces.",
        "formulas": ["force = mass x acceleration", "weight = mass x gravity"],
        "additional_info": "Forces can be either balanced (resulting in no motion) or unbalanced (resulting in acceleration)."
    },
    "energy": {
        "definition": "Energy is the ability of an object to do work. It can come in many forms, including kinetic energy, potential energy, and thermal energy.",
        "subtopics": {
            "kinetic energy": {
                "definition": "Kinetic energy is the energy an object possesses due to its motion. It is proportional to the object's mass and the square of its velocity.",
                "formulas": ["kinetic energy = 0.5 x mass x velocity^2"],
                "additional_info": "Kinetic energy is a scalar quantity, meaning it has no direction. It is always positive, and can never be negative."
            },
            "potential energy": {
                "definition": "Potential energy is the energy an object possesses due to its position or configuration. It can be gravitational potential energy, elastic potential energy, or electric potential energy.",
                "formulas": ["gravitational potential energy = mass x gravity x height", "elastic potential energy = 0.5 x spring constant x displacement^2"],
                "additional_info": "Potential energy can be converted into kinetic energy, and vice versa. The total energy (kinetic + potential) of a system is always conserved."
            },
            "thermal energy": {
                "definition": "Thermal energy is the energy associated with the motion of atoms and molecules in a substance. It can be transferred from one object to another through conduction, convection, or radiation.",
                "formulas": ["heat energy = mass x specific heat capacity x change in temperature"],
                "additional_info": "Temperature is a measure of the average kinetic energy of the particles in a substance. The greater the temperature, the greater the thermal energy."
            },
            "nuclear energy": {
                "definition": "Nuclear energy is the energy released during nuclear reactions, such as fission and fusion. It is one of the most powerful forms of energy, and is used in nuclear power plants and nuclear weapons.",
                "formulas": ["E = mc^2"],
                "additional_info": "The equation E = mc^2, where E is energy, m is mass, and c is the speed of light, relates mass and energy. It shows that a small amount of mass can be converted into a large amount of energy."
            }
        }
    },
    "waves": {
        "definition": "Waves are disturbances that propagate through a medium. Some common types of waves include sound waves, light waves, and water waves.",
        "formulas": ["wave speed = frequency x wavelength", "index of refraction = speed of light in vacuum / speed of light in medium

        ],
        "additional_info": "The index of refraction is a measure of how much a material slows down light. It depends on the material's properties and the frequency of the light."
    }
}

# Function to display information based on user input
def display_info(topic):
    # Check if the topic is a top-level category
    if topic in physics_info:
        print(physics_info[topic]["definition"])
        print("Formulas:")
        for formula in physics_info[topic]["formulas"]:
            print("- " + formula)
        if "additional_info" in physics_info[topic]:
            print("Additional Information:")
            print(physics_info[topic]["additional_info"])
        if "subtopics" in physics_info[topic]:
            print("Subtopics:")
            for subtopic in physics_info[topic]["subtopics"]:
                print("- " + subtopic)
        print()
    # Check if the topic is a subtopic of a top-level category
    elif "." in topic:
        main_topic, subtopic = topic.split(".")
        print(physics_info[main_topic]["subtopics"][subtopic]["definition"])
        print("Formulas:")
        for formula in physics_info[main_topic]["subtopics"][subtopic]["formulas"]:
            print("- " + formula)
        if "additional_info" in physics_info[main_topic]["subtopics"][subtopic]:
            print("Additional Information:")
            print(physics_info[main_topic]["subtopics"][subtopic]["additional_info"])
        print()
    # If the topic is not found, display an error message
    else:
        print("Sorry, that topic is not available. Please try again.")
        print()

# Main program loop
while True:
    # Get user input
    print("Enter a topic to learn more about:")
    topic = input()
    print()
    # Check if user wants to quit
    if topic == "q":
        break
    # Display information based on user input
    display_info(topic)

