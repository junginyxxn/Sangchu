package com.sc.sangchu.postgresql.repository;

import com.sc.sangchu.postgresql.entity.CommResidentPopulationEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CommResidentPopulationRepository extends JpaRepository<CommResidentPopulationEntity, Integer> {
    CommResidentPopulationEntity findByCommercialDistrictCodeAndYearCodeAndQuarterCode(Long commCode, Integer year, Integer quarter);
    List<CommResidentPopulationEntity> findAllByCommercialDistrictCode(Long commCode);
    List<CommResidentPopulationEntity> findByYearCodeAndQuarterCodeAndCommercialDistrictCode(int year, int quarter, Long[] commList);
}