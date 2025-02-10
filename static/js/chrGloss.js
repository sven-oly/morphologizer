// Javascipt specific to Cherokee gloss

function change_generate_option(selection, gloss_part) {
    // Get the value
    let params = get_generate_parameters();

    // Handle special restrictions based on selection and gloss part.
    let was_changed = apply_restrictions(selection, gloss_part);

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


function apply_restrictions(selection, gloss_part) {
    // Disable some settings based on particular values.
    let result;

    if (gloss_part == 'prefix') {
        result = fix_prefixes(selection, gloss_part, selection.value);
    return result;
    }

    if (gloss_part == 'stem form') {
        result = fix_stem_form(selection, gloss_part, selection.value);
    return result;
    }

    // Other things, too.
}

function fix_prefixes(selection, gloss_part, value) {
    let changed;
    let this_val = selection.value;
    let is_on = selection.checked;
    

    // Check for incompatibility of IRR vs. REL.
    if (this_val == 'IRR') {
        changed = turn_off_other_options(gloss_part, ['REL', 'NGT'], is_on);
    } else if (this_val == 'REL') {
        changed = turn_off_other_options(gloss_part, ['IRR', 'NGT'], is_on);
    } else if (this_val == 'NGT') {
        changed = turn_off_other_options(gloss_part, ['IRR', 'REL'], is_on);
    }
    return changed;
}

function fix_prefixes(selection, gloss_part, value) {
    let changed;
    let this_val = selection.value;
    let is_on = selection.checked;
    
    // Check for incompatibility of IRR vs. REL.
    if (this_val == 'IRR') {
        changed = turn_off_other_options(gloss_part, ['REL', 'NGT'], is_on);
    } else if (this_val == 'REL') {
        changed = turn_off_other_options(gloss_part, ['IRR', 'NGT'], is_on);
    } else if (this_val == 'NGT') {
        changed = turn_off_other_options(gloss_part, ['IRR', 'REL'], is_on);
    }
    return changed;
}

function fix_stem_form(selection, gloss_part, value) {
    let changed;
    let this_val = selection.value;
    let is_on = selection.checked;
    let other_part = 'stem and final';

    // Check for incompatibility of IRR vs. REL.
    if (this_val == 'PresCont' || this_val == 'Immediate') {
        // All the suffixes
        changed = turn_off_other_options(
            other_part,
            ['AbsFut','ExpPast', 'NomAbilityOrObligation', 'NomAbility','NonExpPast'],
             is_on);
    } else if (this_val == 'Incompletive') {
        // All the suffixes
        changed = turn_off_other_options(
            other_part,
            ['NomAbilityOrObligation', 'NomAbility'],
            is_on);
        enable_other_options(
            other_part,
            ['AbsFut','ExpPast', 'NonExpPast'], false);
    } else if (this_val == 'Completive') {
        changed = turn_off_other_options(
            other_part,
            ['NomAbilityOrObligation', 'NomAbility'],
             is_on);
        enable_other_options(other_part,
                             ['AbsFut','ExpPast', 'NonExpPast'], false);
    } else if (this_val == 'DeVerbalNoun') {
        changed = turn_off_other_options(
            other_part,
            ['AbsFut', 'ExpPast', 'NonExpPast'],
             is_on);
        enable_other_options(other_part,
                             ['NomAbilityOrObligation', 'NomAbility'],
                             false);
    }
    return changed;
}

function turn_off_other_options(gloss_part, other_option_list, is_on) {
    let changed;
    for (const term of other_option_list) {
        const other_selector = document.getElementById(gloss_part + '_' + term);
        changed = changed || (other_selector.checked == is_on);
        if (other_selector.checked) {
            other_selector.checked = false;
        }
        other_selector.disabled = is_on;
    }
}

function enable_other_options(gloss_part, enable_list, new_val) {
    let changed;
    for (const term of enable_list) {
        const other_id = gloss_part + '_' + term;
            const other_selector = document.getElementById(other_id);
        other_selector.disabled = new_val;
    }
}
