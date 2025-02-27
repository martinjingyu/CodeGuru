def generate_badges(text):
    # Generate inline style badge HTML
    inline_html = f'''
    <span style="display: inline-block; padding: 5px 10px; color: white; background-color: #007bff; border-radius: 5px;">
        {text}
    </span>
    '''

    # Generate overlay style badge HTML
    overlay_html = f'''
    <div style="position: relative; padding: 20px;">
        <span style="display: inline-block; padding: 5px 10px; color: white; background-color: #28a745; border-radius: 5px;">
            {text}
        </span>
    </div>
    '''

    return inline_html, overlay_html

def main():
    # Accept user input
    user_text = input("Enter the text for the badges: ")

    # Generate badges
    inline_badge, overlay_badge = generate_badges(user_text)

    # Output the generated HTML
    print("\nInline Style Badge HTML:")
    print(inline_badge)

    print("\nOverlay Style Badge HTML:")
    print(overlay_badge)

    print("\nFull HTML to visualize:")
    full_html = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Badges Demo</title>
    </head>
    <body>
        {inline_badge}
        <br><br>
        {overlay_badge}
    </body>
    </html>
    '''
    print(full_html)

if __name__ == "__main__":
    main()