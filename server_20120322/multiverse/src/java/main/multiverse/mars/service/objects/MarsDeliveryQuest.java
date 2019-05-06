package java.main.multiverse.mars.service.objects;

public class MarsDeliveryQuest extends MarsQuest {
    public MarsDeliveryQuest() {
        super();
    }

    public void setDeliveryTarget(MarsMob mob) {
        deliveryTarget = mob;
    }
    public MarsMob getDeliveryTarget() {
        return deliveryTarget;
    }
    MarsMob deliveryTarget = null;

    public DeliveryQuestState generate(Long playerOid) {
	throw new RuntimeException("not implemented");
    }

    private static final long serialVersionUID = 1L;
}
