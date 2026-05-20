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
        <DefinitionItem term="Senior/Key Personnel">
          The PD/PI and any other person identified as senior/key personnel by the Company in the grant
          application, progress report, or any other report submitted to NIH by the Company under this regulation.
        </DefinitionItem>
        <DefinitionItem term="Significant Financial Interest (SFI)">
          A financial interest consisting of one or more of the following interests of the Investigator (and those
          of the Investigator's spouse and dependent children) that reasonably appears to be related to the
          Investigator's institutional responsibilities:
        </DefinitionItem>
        <ul style={{ paddingLeft: '2rem', marginBottom: '1rem', lineHeight: '1.8' }}>
          <li>
            With regard to any <strong>publicly traded entity</strong>, an SFI exists if the value of any
            remuneration received from the entity in the twelve months preceding the disclosure and the value of
            any equity interest in the entity as of the date of disclosure, when aggregated, exceeds $5,000.
          </li>
          <li>
            With regard to any <strong>non-publicly traded entity</strong>, an SFI exists if the value of any
            remuneration received from the entity in the twelve months preceding the disclosure, when aggregated,
            exceeds $5,000, or when the Investigator (or the Investigator's spouse or dependent children) holds
            any equity interest (e.g., stock, stock option, or other ownership interest).
          </li>
          <li>
            Intellectual property rights and interests (e.g., patents, copyrights), upon receipt of income related
            to such rights and interests.
          </li>
          <li>
            Any reimbursed or sponsored travel related to the Investigator's institutional responsibilities,
            excluding travel reimbursed or sponsored by a U.S. federal, state, or local government agency, a U.S.
            institution of higher education as defined at 20 U.S.C. 1001(a), an academic teaching hospital, a
            medical center, or a research institute that is affiliated with a U.S. institution of higher education.
          </li>
        </ul>

        <div style={{
          background: '#f0f7fd',
          border: '1px solid var(--primary-3)',
          borderRadius: '0.4rem',
          padding: '1rem 1.25rem',
          marginBottom: '1rem',
        }}>
          <p style={{ fontWeight: '600', marginBottom: '0.5rem' }}>
            Important Note Regarding Foreign Financial Interests:
          </p>
          <p>
            The exclusions listed above for income from government agencies, institutions of higher education,
            academic teaching hospitals, medical centers, and affiliated research institutes apply only to United
            States entities. Investigators must disclose all financial interests received from foreign institutions
            of higher education or the government of another country (including any local, provincial, or
            equivalent government of another country) when such income meets the applicable threshold for
            disclosure (e.g., remuneration in excess of $5,000). This includes, but is not limited to, income from
            foreign seminars, lectures, teaching engagements, advisory committees, review panels, and reimbursed
            or sponsored travel paid by or on behalf of a foreign entity. See NIH FAQs E.9., E.20., E.21., E.24.,
            E.36., and E.37. for further guidance.
          </p>
        </div>

        <p style={{ marginBottom: '0.5rem' }}><strong>SFI does not include:</strong></p>
        <ul style={{ paddingLeft: '2rem', marginBottom: '1rem', lineHeight: '1.8' }}>
          <li>Salary, royalties, or other remuneration paid by the Company to the Investigator if the Investigator is currently employed or otherwise appointed by the Company;</li>
          <li>Intellectual property rights assigned to the Company and agreements to share in royalties related to such rights;</li>
          <li>Any ownership interest in the Company held by the Investigator, if the Company is an applicant under the SBIR/STTR programs;</li>
          <li>Income from investment vehicles such as mutual funds and retirement accounts, as long as the Investigator does not directly control the investment decisions made in these vehicles;</li>
          <li>Income from seminars, lectures, or teaching engagements sponsored by, or from advisory committees or review panels for, a U.S. federal, state, or local government agency, a U.S. institution of higher education as defined at 20 U.S.C. 1001(a), an academic teaching hospital, a medical center, or a research institute affiliated with a U.S. institution of higher education. <em>Note: This exclusion does not apply to income received from foreign entities (see note above).</em></li>
        </ul>
      </Section>

      <Section title="4. Institutional Official">
        <p>
          The President and Chief Technology Officer of ZwiCoat Materials Innovations, LLC serves as the
          Institutional Official and is responsible for the implementation, oversight, and enforcement of this
          Policy. The Institutional Official's responsibilities include, but are not limited to:
        </p>
        <ul style={{ paddingLeft: '2rem', marginTop: '0.75rem', lineHeight: '1.8' }}>
          <li>Informing each Investigator of this Policy, the Investigator's disclosure obligations regarding all foreign and domestic significant financial interests, and the federal regulation (42 CFR Part 50, Subpart F);</li>
          <li>Soliciting and reviewing Investigator SFI disclosures;</li>
          <li>Determining whether disclosed SFIs are related to PHS-funded research and whether they constitute FCOIs;</li>
          <li>Developing and implementing management plans for identified FCOIs;</li>
          <li>Reporting identified FCOIs to the NIH through the eRA Commons FCOI Module;</li>
          <li>Ensuring Investigator compliance with this Policy and applicable management plans;</li>
          <li>Maintaining records of all disclosures and actions taken;</li>
          <li>Ensuring that training requirements are met; and</li>
          <li>Making FCOI and SFI information, including related institutional reviews and determinations, available to the NIH promptly upon request.</li>
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
          Investigator's responsibilities regarding disclosure of all foreign and domestic SFIs. The{' '}
          <a
            href="https://grants.nih.gov/grants/policy/coi/tutorial2011/fcoi.htm"
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: 'var(--primary-1)' }}
          >
            NIH FCOI Training Module
          </a>{' '}
          may be used to satisfy the regulatory training requirement. Upon completion, certificates of completion
          must be provided to the Institutional Official. The Company will also provide training on this Policy
          and the Investigator's disclosure requirements.
        </p>
      </Section>

      <Section title="6. Disclosure of Significant Financial Interests">
        <p>
          Each Investigator must disclose to the Institutional Official all Significant Financial Interests, both
          foreign and domestic (and those of the Investigator's spouse and dependent children), related to the
          Investigator's institutional responsibilities. Disclosures must be made using the Company's SFI Disclosure
          Form and are required at the following times:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>No later than at the time of application for PHS-funded research;</li>
          <li>At least annually during the period of an award (within 30 days of the anniversary of the initial disclosure); and</li>
          <li>Within 30 days of discovering or acquiring (e.g., through purchase, marriage, or inheritance) a new SFI.</li>
        </ul>
        <p>
          Investigators must also disclose the occurrence of any reimbursed or sponsored travel related to their
          institutional responsibilities (as defined in Section 3), including the purpose of the trip, the identity
          of the sponsor/organizer, the destination, and the duration. This includes travel reimbursed or sponsored
          by foreign entities, foreign institutions of higher education, and foreign governments.
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
          include:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>Grant number and project title;</li>
          <li>PD/PI name;</li>
          <li>Name of the Investigator with the FCOI;</li>
          <li>Name of the entity with which the Investigator has an FCOI;</li>
          <li>Nature of the financial interest (e.g., equity, consulting fees, intellectual property);</li>
          <li>Value of the financial interest (reported in the dollar ranges specified by NIH: $0–4,999; $5,000–9,999; $10,000–19,999; amounts between $20,000–100,000 by increments of $20,000; amounts above $100,000 by increments of $50,000), or a statement that the value cannot be readily determined;</li>
          <li>A description of how the financial interest relates to the PHS-funded research and the basis for the Company's determination that the interest is an FCOI;</li>
          <li>The role and principal duties of the conflicted Investigator in the research project; and</li>
          <li>Key elements of the management plan.</li>
        </ul>

        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.2 Annual FCOI Report</h3>
        <p>
          The Company will submit an annual FCOI report to the NIH for the duration of the project period regarding
          any previously reported FCOI and the status of the management plan. The annual report will specify
          whether the FCOI is still being managed, explain any changes to the management plan, and confirm
          Investigator compliance.
        </p>

        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.3 Revised FCOI Report</h3>
        <p>
          For any newly identified FCOI during an ongoing project, the Company will submit an FCOI report to the
          NIH within 60 days of identification.
        </p>

        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.4 Notification of Noncompliance</h3>
        <p>
          The Company will notify the NIH promptly if an Investigator (or subrecipient Investigator) fails to
          comply with this Policy, or if noncompliance with an FCOI management plan appears to have biased the
          design, conduct, or reporting of PHS-funded research. The Company will take corrective action promptly
          upon identification of any noncompliance.
        </p>

        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1rem' }}>9.5 Cooperation with NIH</h3>
        <p>
          The Company agrees to make FCOI and SFI information, including related institutional reviews and
          determinations, available to the NIH promptly upon request.
        </p>
      </Section>

      <Section title="10. Retrospective Review">
        <p>
          If the Company identifies an SFI that was not disclosed in a timely manner by an Investigator, or was
          not previously reviewed by the Company, the Institutional Official will, within 60 days, review the SFI,
          determine whether it constitutes an FCOI, and if so, implement an interim management plan. In addition,
          whenever an FCOI is not identified or managed in a timely manner, the Company will complete a
          retrospective review of the Investigator's activities and the PHS-funded research project within 120 days
          to determine whether any PHS-funded research conducted during the period of noncompliance was biased in
          the design, conduct, or reporting of such research.
        </p>
        <p>The retrospective review will be documented and will include, at a minimum:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>Project number and project title;</li>
          <li>PD/PI or contact PD/PI if a multiple PD/PI model is used;</li>
          <li>Name of the Investigator with the FCOI;</li>
          <li>Name of the entity with which the Investigator has an FCOI;</li>
          <li>Reasons for the retrospective review;</li>
          <li>Detailed methodology used for the retrospective review (e.g., methodology of the review process, composition of the review panel, documentation reviewed);</li>
          <li>Findings of the review; and</li>
          <li>Conclusions of the review.</li>
        </ul>
        <p>
          If the retrospective review determines that the PHS-funded research was biased, the Company will notify
          the NIH promptly and submit a mitigation report that includes the key elements of the retrospective
          review listed above, plus a description of the impact of the bias on the research project and a plan of
          action or description of actions taken to eliminate or mitigate the effect of the bias.
        </p>

        <h3 style={{ fontWeight: '600', marginBottom: '0.5rem', marginTop: '1.25rem' }}>10.1 Clinical Research Disclosure Requirement</h3>
        <p>
          In any case in which the Department of Health and Human Services determines that a PHS-funded clinical
          research project whose purpose is to evaluate the safety or effectiveness of a drug, medical device, or
          treatment has been designed, conducted, or reported by an Investigator with an FCOI that was not managed
          or reported as required by this Policy, the Company shall require the Investigator to:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>Disclose the FCOI in each public presentation of the results of the research; and</li>
          <li>Request an addendum to previously published presentations.</li>
        </ul>
      </Section>

      <Section title="11. Subrecipient Requirements">
        <p>
          When the Company enters into a subaward agreement with a subrecipient for PHS-funded research, the
          written agreement will specify whether the subrecipient's Investigators will comply with this Policy or
          the subrecipient's own FCOI policy. If the subrecipient's Investigators will follow the subrecipient's
          own policy, the subrecipient must certify that its policy complies with 42 CFR Part 50, Subpart F. The
          subaward agreement will specify time periods for the subrecipient to report identified FCOIs to the
          Company, which must be sufficient to enable the Company to report to NIH in a timely manner.
        </p>
        <p>
          If the subrecipient cannot make such a certification, the agreement will state that the subrecipient's
          Investigators are subject to this Policy for disclosing SFIs that are directly related to the
          subrecipient's work for the Company.
        </p>
      </Section>

      <Section title="12. Public Accessibility">
        <p>
          This Policy is publicly accessible on the Company's website and has been submitted to the NIH via the
          eRA Commons Institution Profile (IPF) Module, as required by NOT-OD-21-002. The Company will update the
          posted policy and resubmit to NIH whenever the Policy is revised.
        </p>
        <p>
          If requested, the Company will make this Policy available to any individual within five business days of
          the request. In addition, information concerning any Investigator's SFI determined to be an FCOI held by
          Senior/Key Personnel (as defined in Section 3) will be made publicly accessible prior to the expenditure
          of funds. The Company will make such information available via written request, responding within five
          business days. The information made available will include, at a minimum:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.75rem 0', lineHeight: '1.8' }}>
          <li>The Investigator's name;</li>
          <li>The Investigator's title and role with respect to the research project;</li>
          <li>The name of the entity in which the SFI is held;</li>
          <li>The nature of the SFI; and</li>
          <li>The approximate dollar value of the SFI, or a statement that the interest is one whose value cannot be readily determined through reference to public prices or other reasonable measures of fair market value.</li>
        </ul>
        <p>
          This publicly accessible information will be updated at least annually, updated within sixty (60) days of
          a newly identified FCOI, and will remain available for at least three (3) years from the date the
          information was most recently updated.
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
          response to such disclosures (whether or not a disclosure resulted in a determination of an FCOI), all
          actions taken under this Policy, and any retrospective reviews, for a period of at least three years from
          the date the final expenditure report is submitted to the PHS, or as otherwise required by 2 CFR 200.334.
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
          <li>NIH Guide Notice NOT-OD-22-210 – Financial Conflict of Interest and Other Support: Reminders</li>
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
    <h2 style={{
      fontSize: '1.1rem',
      fontWeight: '700',
      color: 'var(--primary-1)',
      borderBottom: '1px solid var(--grey-light)',
      paddingBottom: '0.4rem',
      marginBottom: '0.9rem',
      textTransform: 'uppercase',
      letterSpacing: '0.05em',
    }}>
      {title}
    </h2>
    <div style={{ lineHeight: '1.75', color: 'var(--grey-darkest)', display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
      {children}
    </div>
  </section>
);

const DefinitionItem = ({ term, children }) => (
  <p><strong>{term}:</strong> {children}</p>
);

export default FCOI;
