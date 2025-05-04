for index, row in df.iterrows():
    total_marks = row['Total Marks']

    # Ensure it's numeric (if not, set to 0)
    try:
        total_marks = int(total_marks)
    except (ValueError, TypeError):
        total_marks = 0

    # Initialize Part A and Part B
    part_a = [0] * 5
    part_b = [0] * 5

    if total_marks <= 5:
        # Distribute total_marks randomly across 5 Part A questions (max 2 per question)
        remaining = total_marks
        while remaining > 0:
            available = [idx for idx in range(5) if part_a[idx] < 2]
            if not available:
                break
            pick = random.choice(available)
            part_a[pick] += 1
            remaining -= 1
        part_a_total = sum(part_a)
        part_b_total = 0  # No marks left for Part B

    else:
        # Part A: Random 0-2 marks per question
        part_a = [random.randint(0, 2) for _ in range(5)]
        part_a_total = sum(part_a)

        # Part B: Remaining marks
        remaining = total_marks - part_a_total

        # Distribute remaining marks across 5 Part B questions (max 8 per question)
        while remaining > 0:
            available = [idx for idx in range(5) if part_b[idx] < 8]
            if not available:
                break
            pick = random.choice(available)
            part_b[pick] += 1
            remaining -= 1
        part_b_total = sum(part_b)

    results.append({
        'Total Marks': total_marks,
        'Part A Q1': part_a[0],
        'Part A Q2': part_a[1],
        'Part A Q3': part_a[2],
        'Part A Q4': part_a[3],
        'Part A Q5': part_a[4],
        'Part A Total': part_a_total,
        'Part B Q1': part_b[0],
        'Part B Q2': part_b[1],
        'Part B Q3': part_b[2],
        'Part B Q4': part_b[3],
        'Part B Q5': part_b[4],
        'Part B Total': part_b_total,
    })
