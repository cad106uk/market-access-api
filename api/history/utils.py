def get_changed_fields(new_record, old_record):
    if hasattr(new_record, "get_changed_fields"):
        return new_record.get_changed_fields(old_record)
    return new_record.diff_against(old_record).changed_fields


def get_model_name(history_instance):
    object_name = history_instance.instance_type._meta.object_name
    return {
        "Assessment": "assessment",
        "BarrierInstance": "barrier",
        "Interaction": "note",
        "PublicBarrier": "public_barrier",
        "PublicBarrierNote": "public_barrier_note",
        "TeamMember": "team_member",
        "WTOProfile": "wto_profile",
    }.get(object_name)