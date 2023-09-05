from ecs import EntityManager, SystemManager

entity_manager_object = EntityManager()
system_manager_object = SystemManager(entity_manager_object)