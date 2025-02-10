// Javascipt specific to Cherokee gloss

function change_generate_option(selection, gloss_part) {
    // Get the value
    let params = get_generate_parameters();


    // Combine parameters and make into a string
    let prefix = '';
    let prefixes = [];
    let verb_part = '';
    let stem_form;
    let stem_element = document.getElementById('stem_text_area');
    let stem = stem_element.value;
    let word_type = '[V]';
    let stem_final;
    // Special cases
    for (const param of params) {
        const gloss_type = param[0];
        const val = param[1];
        if (gloss_type == 'prefix') {
            // Handle multiple values - how??
            prefix += val;
            prefixes.push('[' + val + ']');
        } else if (gloss_type == 'subject') {
            verb_part = val;
        } else if (gloss_type == 'object' && val != "None") {
            verb_part += '/' + val;
        } else if (gloss_type == 'stem form' && val != "None" ) {
            stem_form = val ;
        } else if (gloss_type == 'stem and final' && val != "None") {
            stem_final = val;
        }
    }
    let output_items = [];
    if (prefix) {
        for (p of prefixes) {
            output_items.push(p);
        }
        // output_items.push('[' + prefix + ']');
    }
    output_items.push('[' + verb_part + ']');
    output_items.push(stem);
    output_items.push(word_type);
    if (stem_form) {
        output_items.push('[' + stem_form + ']');
    }
    if (stem_final) {
        output_items.push('[' + stem_final + ']');
    }
    
    // Ready to push it out.
    const output_element = document.getElementById('gen_text');
    const output_string = output_items.join('+');  // TODO: Fix this!
    output_element.value = output_string;
}

