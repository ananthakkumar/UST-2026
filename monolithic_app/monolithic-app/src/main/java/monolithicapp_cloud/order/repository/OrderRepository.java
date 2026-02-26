package monolithicapp_cloud.order.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import monolithicapp_cloud.order.entity.Order;

public interface OrderRepository extends JpaRepository<Order, Long> {
}