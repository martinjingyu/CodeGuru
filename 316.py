import ssl

def setup_ssl_context(modify_settings=False):
    """
    Set up an SSL context with default options.
    
    :param modify_settings: If True, apply settings that may reduce security.
    :return: An SSL context.
    """

    # Create a default SSL context
    context = ssl.create_default_context()

    if modify_settings:
        # Disable certificate verification - Insecure! Only for testing or specific trusted environments.
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # Allow older, less secure protocols and ciphers - Insecure!
        context.options &= ~ssl.OP_NO_SSLv3
        context.options &= ~ssl.OP_NO_SSLv2
        context.options &= ~ssl.OP_NO_TLSv1
        context.options &= ~ssl.OP_NO_TLSv1_1

        # Use a specific cipher suite that may not be secure - Insecure!
        context.set_ciphers('ALL:@SECLEVEL=1')

        print("Warning: Modifying SSL settings to potentially insecure values.")

    return context

# Example usage:
# context_default = setup_ssl_context()
# context_insecure = setup_ssl_context(modify_settings=True)