career_paths = {
    "STEM": ["logic", "technology", "experiments", "coding", "math", "problem-solving"],
    "Arts": ["creativity", "painting", "writing", "music", "storytelling"],
    "Sports": ["fitness", "teamwork", "competition", "stamina"],
    "Business": ["leadership", "management", "finance", "strategy"],
    "Healthcare": ["helping", "biology", "medicine", "care"],
}

explanations = {
    "STEM": "Great for logical thinkers who enjoy technology and experimentation.",
    "Arts": "Ideal for expressive individuals who love creativity and storytelling.",
    "Sports": "Perfect for those passionate about physical activity and discipline.",
    "Business": "Suits planners and leaders interested in finance and operations.",
    "Healthcare": "For compassionate individuals interested in medicine and care.",
}

def map_to_career_path(user_input):
    matched_paths = []
    for path, keywords in career_paths.items():
        if any(k.lower() in user_input.lower() for k in keywords):
            matched_paths.append(path)
    return matched_paths or ["Undetermined"]

def generate_explanation(paths):
    return "\n\n".join(
        f"**{path}**: {explanations.get(path, 'A promising path based on your interests.')}"
        for path in paths
    )

def needs_clarification(mapped_paths):
    return "Undetermined" in mapped_paths or not mapped_paths
