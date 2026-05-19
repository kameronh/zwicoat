import React from 'react';

const FCOI = () => {
  return (
    <div style={{ maxWidth: '860px', margin: '0 auto', padding: '3rem 2rem 5rem' }}>
      <h1 style={{ fontSize: '1.75rem', fontWeight: '700', marginBottom: '0.5rem', color: 'var(--grey-darkest)' }}>
        Financial Conflict of Interest (FCOI) Policy
      </h1>
      <p style={{ color: 'var(--grey-darker)', marginBottom: '0.25rem' }}>
        ZwiCoat Materials Innovations, LLC
      </p>
      <p style={{ color: 'var(--grey-darker)', marginBottom: '0.25rem' }}>
        Pursuant to 42 CFR Part 50, Subpart F
      </p>
      <p style={{ color: 'var(--grey-darker)', marginBottom: '2.5rem' }}>
        <strong>Effective Date:</strong> May 1, 2026
      </p>

      <Section title="1. Purpose">
        <p>
          This Financial Conflict of Interest (FCOI) Policy of ZwiCoat Materials Innovations, LLC ("the Company" or
          "ZCMI") is established to comply with the requirements of the 2011 revised regulation, 42 CFR Part 50,
          Subpart F, "Promoting Objectivity in Research," as applicable to National Institutes of Health (NIH) grants
          and cooperative agreements. This Policy promotes objectivity in research by establishing standards that
          provide a reasonable expectation that the design, conduct, and reporting of research funded by the Public
          Health Service (PHS), including NIH, will be free from bias resulting from Investigator financial conflicts
          of interest.
        </p>
        <p>
          This Policy applies to all NIH-funded grants and cooperative agreements, excluding Phase I Small Business
          Innovation Research (SBIR) and Small Business Technology Transfer (STTR) applications and awards.
        </p>
      </Section>

      <Section title="2. Scope and Applicability">
        <p>
          This Policy applies to all Investigators, as defined in Section 3, who are planning to participate in or
          are participating in PHS-funded research conducted by or through the Company. This includes, but is not
          limited to, the Principal Investigator (PI), Co-Principal Investigators (Co-PIs), and any other person
          regardless of title or position who is responsible for the design, conduct, or reporting of PHS-funded
          research, which may include collaborators, consultants, and subrecipient investigators subject to this
          Policy.
        </p>
      </Section>

      <Section title="3. Definitions">
        <DefinitionItem term="Financial Conflict of Interest (FCOI)">
          A Significant Financial Interest (SFI) that the Company reasonably determines could directly and
          significantly affect the design, conduct, or reporting of PHS-funded research.
        </DefinitionItem>
        <DefinitionItem term="Financial Interest">
          Anything of monetary value, whether or not the value is readily ascertainable.
        </DefinitionItem>
        <DefinitionItem term="Institutional Official">
          The President and Chief Technology Officer of ZwiCoat Materials Innovations, LLC, or his/her designee,
          who is responsible for the implementation and oversight of this Policy.
        </DefinitionItem>
        <DefinitionItem term="Institutional Responsibilities">
          An Investigator's professional responsibilities on behalf of the Company, including but not limited to
          activities such as research, research consultation, teaching, professional practice, institutional
          committee memberships, and service on panels such as Institutional Review Boards or Data and Safety
          Monitoring Boards.
        </DefinitionItem>
        <DefinitionItem term="Investigator">
          The project director or principal investigator and any other person, regardless of title or position,
          who is responsible for the design, conduct, or reporting of research funded by the PHS, or proposed for
          such funding. This may include, for example, collaborators or consultants.
        </DefinitionItem>
        <DefinitionItem term="PHS-Funded Research">
          Research funded by the Public Health Service (e.g., NIH) by means of a grant or cooperative agreement,
          excluding Phase I SBIR/STTR applications and awards.
        </DefinitionItem>
        <DefinitionItem term="Significant Financial Interest (SFI)">
          A financial interest consisting of one or more of the following interests of the Investigator (and those
          of the Investigator's spouse and dependent children) that reasonably appears to be related to the
          Investigator's institutional responsibilities:
        </DefinitionItem>
        <ul style={{ paddingLeft: '2rem', marginBottom: '1rem', lineHeight: '1.8' }}>
          <li>
            With regard to any <strong>publicly traded entity</strong>, an SFI exists if the value of any remuneration
            received from the entity in the twelve months preceding the disclosure and the value of any equity
            interest in the entity as of the date of disclosure, when aggregated, exceeds $5,000.
          </li>
          <li>
            With regard to any <strong>non-publicly traded entity</strong>, an SFI exists if the value of any
            remuneration received from the entity in the twelve months preceding the disclosure, when aggregated,
            exceeds $5,000, or when the Investigator (or the Investigator's spouse or dependent children) holds any
            equity interest (e.g., stock, stock option, or other ownership interest).
          </li>
          <li>
            Intellectual property rights and interests (e.g., patents, copyrights), upon receipt of income related
            to such rights and interests.
          </li>
          <li>
            Any reimbursed or sponsored travel related to the Investigator's institutional responsibilities,
            excluding travel reimbursed or sponsored by a federal, state, or local government agency, an institution
            of higher education, an academic teaching hospital, a medical center, or a research institute affiliated
            with an institution of higher education.
          </li>
        </ul>
        <p style={{ marginBottom: '0.5rem' }}>
          <strong>SFI does not include:</strong>
        </p>
        <ul style={{ paddingLeft: '2rem', marginBottom: '1rem', lineHeight: '1.8' }}>
          <li>Salary, royalties, or other remuneration paid by the Company to the Investigator if the Investigator is currently employed or otherwise appointed by the Company;</li>
          <li>Intellectual property rights assigned to the Company and agreements to share in royalties related to such rights;</li>
          <li>Any ownership interest in the Company held by the Investigator, if the Company is an applicant under the SBIR/STTR programs;</li>
          <li>Income from investment vehicles such as mutual funds and retirement accounts, as long as the Investigator does not directly control the investment decisions made in these vehicles;</li>
          <li>Income from seminars, lectures, or teaching engagements sponsored by, or from advisory committees or review panels for, a federal, state, or local government agency, an institution of higher education, an academic teaching hospital, a medical center, or a research institute affiliated with an institution of higher education.</li>
        </ul>
      </Section>

      <Section title="4. Institutional Official">
        <p>
          The President and Chief Technology Officer of ZwiCoat Materials Innovations, LLC serves as the
          Institutional Official and is responsible for the implementation, oversight, and enforcement of this
          Policy. The Institutional Official's responsibilities include, but are not limited to:
        </p>
        <ul style={{ paddingLeft: '2rem', marginTop: '0.75rem', lineHeight: '1.8' }}>
          <li>Informing each Investigator of this Policy, the Investigator's disclosure obligations, and the federal regulation (42 CFR Part 50, Subpart F);</li>
          <li>Soliciting and reviewing Investigator SFI disclosures;</li>
          <li>Determining whether disclosed SFIs are related to PHS-funded research and whether they constitute FCOIs;</li>
          <li>Developing and implementing management plans for identified FCOIs;</li>
          <li>Reporting identified FCOIs to the NIH through the eRA Commons FCOI Module;</li>
          <li>Ensuring Investigator compliance with this Policy and applicable management plans;</li>
          <li>Maintaining records of all disclosures and actions taken; and</li>
          <li>Ensuring that training requirements are met.</li>
        </ul>
      </Section>

      <Section title="5. Investigator Training">
        <p>
          Each Investigator must complete FCOI training before engaging in PHS-funded research and at least every
          four years thereafter. Training must also be completed:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>When the Company revises this FCOI Policy in any manner that affects the requirements of Investigators;</li>
          <li>When an Investigator is new to the Company; and</li>
          <li>When the Company finds that an Investigator is not in compliance with this Policy or a management plan.</li>
        </ul>
        <p>
          Training shall cover the federal FCOI regulation (42 CFR Part 50, Subpart F), this Policy, and the
          Investigator's responsibilities regarding disclosure of SFIs. The{' '}
          <a
            href="https://grants.nih.gov/grants/policy/coi/tutorial2011/fcoi.htm"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: 'var(--primary-1)' }}
          >
            NIH FCOI Training Module
          </a>{' '}
          may be used to satisfy the regulatory training requirement. Upon completion, certificates of completion
          must be provided to the Institutional Official.
        </p>
      </Section>

      <Section title="6. Disclosure of Significant Financial Interests">
        <p>
          Each Investigator must disclose to the Institutional Official all Significant Financial Interests (and
          those of the Investigator's spouse and dependent children) related to the Investigator's institutional
          responsibilities. Disclosures must be made using the Company's SFI Disclosure Form and are required at
          the following times:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>No later than at the time of application for PHS-funded research;</li>
          <li>At least annually during the period of an award (within 30 days of the anniversary of the initial disclosure); and</li>
          <li>Within 30 days of discovering or acquiring (e.g., through purchase, marriage, or inheritance) a new SFI.</li>
        </ul>
        <p>
          Investigators must also disclose the occurrence of any reimbursed or sponsored travel related to their
          institutional responsibilities, including the purpose of the trip, the identity of the sponsor/organizer,
          the destination, and the duration.
        </p>
      </Section>

      <Section title="7. Review and Determination of FCOI">
        <p>The Institutional Official will review each Investigator's SFI disclosure to determine:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>Whether an Investigator's SFI is related to PHS-funded research (i.e., whether the SFI could be affected by the research, or is in an entity whose financial interest could be affected by the research); and</li>
          <li>If so related, whether the SFI constitutes a Financial Conflict of Interest (i.e., whether the SFI could directly and significantly affect the design, conduct, or reporting of the PHS-funded research).</li>
        </ul>
        <p>
          The Institutional Official will complete this review and any resulting determination prior to the
          expenditure of any PHS funds for the applicable research project. For any SFI that the Investigator did
          not disclose timely or that the Company did not review timely, the Institutional Official will review the
          SFI within 60 days and implement, on at least an interim basis, a management plan.
        </p>
      </Section>

      <Section title="8. Management of Financial Conflicts of Interest">
        <p>
          If the Institutional Official determines that a Financial Conflict of Interest exists, the Institutional
          Official will develop and implement a management plan that specifies the actions to be taken to manage
          the FCOI. Examples of management plan conditions may include, but are not limited to:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>Public disclosure of the FCOI (e.g., when presenting or publishing the research);</li>
          <li>Appointment of an independent monitor capable of taking measures to protect the design, conduct, and reporting of the research against bias;</li>
          <li>Modification of the research plan;</li>
          <li>Change of personnel or personnel responsibilities, or disqualification of Investigators from participation in all or a portion of the research;</li>
          <li>Reduction or elimination of the financial interest; and/or</li>
          <li>Severance of relationships that create the conflict.</li>
        </ul>
        <p>
          The affected Investigator must formally agree to the management plan in writing before participating or
          continuing to participate in the related PHS-funded research. The Institutional Official will monitor
          Investigator compliance with the management plan on an ongoing basis until the completion of the project.
        </p>
      </Section>

      <Section title="9. Reporting to NIH">
        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.1 Initial FCOI Report</h3>
        <p>
          Prior to the expenditure of any funds under a PHS-funded research project, the Company will submit an
          FCOI report to the NIH through the eRA Commons FCOI Module for each identified FCOI. The report will
          include: the grant number and project title; PD/PI name; name of the Investigator with the FCOI; name of
          the entity with which the Investigator has an FCOI; nature of the financial interest; value of the
          financial interest; a description of how the financial interest relates to the PHS-funded research; and
          key elements of the management plan.
        </p>
        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.2 Annual FCOI Report</h3>
        <p>
          The Company will submit an annual FCOI report to the NIH for the duration of the project period regarding
          any previously reported FCOI and the status of the management plan. The annual report will specify whether
          the FCOI is still being managed, explain any changes to the management plan, and confirm Investigator
          compliance.
        </p>
        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.3 Revised FCOI Report</h3>
        <p>
          For any newly identified FCOI during an ongoing project, the Company will submit an FCOI report to the
          NIH within 60 days of identification.
        </p>
      </Section>

      <Section title="10. Retrospective Review">
        <p>
          If the Company identifies an SFI that was not disclosed in a timely manner by an Investigator, or was not
          previously reviewed by the Company, the Institutional Official will, within 60 days, review the SFI,
          determine whether it constitutes an FCOI, and if so, implement an interim management plan.
        </p>
        <p>
          Whenever an FCOI is not identified or managed in a timely manner, the Company will complete a
          retrospective review of the Investigator's activities and the PHS-funded research project within 120 days
          to determine whether any PHS-funded research conducted during the period of noncompliance was biased in
          the design, conduct, or reporting of such research. If bias is found, the Company will notify the NIH
          promptly and submit a mitigation report.
        </p>
      </Section>

      <Section title="11. Subrecipient Requirements">
        <p>
          When the Company enters into a subaward agreement with a subrecipient for PHS-funded research, the
          written agreement will specify whether the subrecipient's Investigators will comply with this Policy or
          the subrecipient's own FCOI policy. If the subrecipient's Investigators will follow the subrecipient's
          own policy, the subrecipient must certify that its policy complies with 42 CFR Part 50, Subpart F.
        </p>
      </Section>

      <Section title="12. Public Accessibility">
        <p>
          This Policy is publicly accessible on the Company's website. If requested, the Company will make this
          Policy available to any individual within five business days of the request. In addition, information
          concerning any Investigator's SFI determined to be an FCOI held by senior/key personnel will be made
          available, upon written request, within five business days. The information made available will include,
          at a minimum: the Investigator's name; title and role with respect to the research project; the name of
          the entity in which the SFI is held; the nature of the SFI; and the approximate dollar value of the SFI.
        </p>
      </Section>

      <Section title="13. Enforcement and Sanctions">
        <p>
          Failure to comply with any aspect of this Policy, including but not limited to failure to disclose SFIs
          timely, failure to complete required training, or failure to comply with a management plan, may result in
          sanctions or administrative actions including, but not limited to:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>Written warning;</li>
          <li>Required retraining;</li>
          <li>Suspension or termination of participation in PHS-funded research;</li>
          <li>Reduction or elimination of the financial interest causing the conflict; and/or</li>
          <li>Other administrative action, up to and including termination of employment or consulting arrangement.</li>
        </ul>
      </Section>

      <Section title="14. Record Retention">
        <p>
          The Company will maintain records of all Investigator SFI disclosures, the Company's review of and
          response to such disclosures, all actions taken under this Policy, and any retrospective reviews, for a
          period of at least three years from the date the final expenditure report is submitted to the PHS, or as
          otherwise required by 2 CFR 200.334.
        </p>
      </Section>

      <Section title="15. Policy Review and Updates">
        <p>
          This Policy will be reviewed at least annually by the Institutional Official and updated as necessary to
          ensure continued compliance with 42 CFR Part 50, Subpart F, and NIH requirements. Any revisions to this
          Policy will be communicated to all Investigators, and retraining will be required as applicable.
        </p>
      </Section>

      <Section title="16. Regulatory References">
        <ul style={{ paddingLeft: '2rem', lineHeight: '1.8' }}>
          <li>42 CFR Part 50, Subpart F – Promoting Objectivity in Research</li>
          <li>45 CFR Part 94 – Responsible Prospective Contractors</li>
          <li>NIH Grants Policy Statement, Section 4.1.10 – Financial Conflict of Interest</li>
          <li>NIH Guide Notice NOT-OD-21-002 – Required Submission of FCOI Policy into eRA Commons IPF Module</li>
        </ul>
      </Section>

      <Section title="17. Contact Information">
        <p>For questions regarding this Policy, please contact the Institutional Official:</p>
        <address style={{ marginTop: '0.75rem', fontStyle: 'normal', lineHeight: '1.8' }}>
          <strong>Kameron Hansen, Ph.D.</strong><br />
          President and Chief Technology Officer<br />
          ZwiCoat Materials Innovations, LLC<br />
          2635 Johnsons XING NE<br />
          Solon, IA 52333<br />
          Phone: (917) 609-4598<br />
          Email:{' '}
          <a href="mailto:kameronh@zwicoat.com" style={{ color: 'var(--primary-1)' }}>
            kameronh@zwicoat.com
          </a>
        </address>
      </Section>
    </div>
  );
};

const Section = ({ title, children }) => (
  <section style={{ marginBottom: '2rem' }}>
    <h2
      style={{
        fontSize: '1.1rem',
        fontWeight: '700',
        color: 'var(--primary-1)',
        borderBottom: '1px solid var(--grey-light)',
        paddingBottom: '0.4rem',
        marginBottom: '0.9rem',
        textTransform: 'uppercase',
        letterSpacing: '0.05em',
      }}
    >
      {title}
    </h2>
    <div style={{ lineHeight: '1.75', color: 'var(--grey-darkest)', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
      {children}
    </div>
  </section>
);

const DefinitionItem = ({ term, children }) => (
  <p>
    <strong>{term}:</strong> {children}
  </p>
);

export default FCOI;
