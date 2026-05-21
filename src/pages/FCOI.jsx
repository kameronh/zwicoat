import React, { useState } from 'react';

const FCOI = () => {
  const [openToc, setOpenToc] = useState(false);

  const sections = [
    { id: 's1', title: '1) Introduction' },
    { id: 's2', title: '2) Applicability' },
    { id: 's3', title: '3) Definitions' },
    { id: 's4', title: '4) SFI Disclosure Requirements' },
    { id: 's5', title: '5) Review of SFI Disclosures' },
    { id: 's6', title: '6) Relatedness of SFIs and FCOI' },
    { id: 's7', title: '7) Management of SFIs that Pose an FCOI' },
    { id: 's8', title: '8) Monitoring Investigator Compliance' },
    { id: 's9', title: '9) Public Accessibility' },
    { id: 's10', title: '10) Reporting Identified FCOIs' },
    { id: 's11', title: '11) Training Requirements' },
    { id: 's12', title: '12) Noncompliance & Corrective Actions' },
    { id: 's13', title: '13) Clinical Research Requirements' },
    { id: 's14', title: '14) Subrecipient Requirements' },
    { id: 's15', title: '15) Maintenance of Records' },
    { id: 's16', title: '16) Enforcement Actions' },
    { id: 's17', title: '17) Useful Resources' },
    { id: 's18', title: '18) Point of Contact' },
  ];

  return (
    <div style={{ maxWidth: '900px', margin: '0 auto', padding: '3rem 2rem 5rem', fontFamily: 'system-ui, sans-serif' }}>

      {/* Header */}
      <h1 style={{ fontSize: '1.75rem', fontWeight: '700', marginBottom: '0.25rem', color: 'var(--grey-darkest)' }}>
        Financial Conflict of Interest (FCOI) Policy
      </h1>
      <p style={{ color: 'var(--grey-darker)', marginBottom: '0.15rem' }}>ZwiCoat Materials Innovations, LLC</p>
      <p style={{ color: 'var(--grey-darker)', marginBottom: '2rem' }}><strong>Effective:</strong> May 21, 2026</p>

      {/* Table of Contents */}
      <div style={{
        background: '#f8fafc',
        border: '1px solid var(--grey-light)',
        borderRadius: '0.5rem',
        marginBottom: '2.5rem',
        overflow: 'hidden',
      }}>
        <button
          onClick={() => setOpenToc(!openToc)}
          style={{
            width: '100%',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '0.85rem 1.25rem',
            background: 'none',
            border: 'none',
            cursor: 'pointer',
            fontWeight: '600',
            color: 'var(--grey-darkest)',
            fontSize: '0.95rem',
          }}
        >
          <span>Table of Contents</span>
          <span style={{ fontSize: '0.8rem', color: 'var(--grey-darker)' }}>{openToc ? '▲ Hide' : '▼ Show'}</span>
        </button>
        {openToc && (
          <ol style={{ margin: '0', padding: '0 1.25rem 1rem 2.5rem', lineHeight: '2' }}>
            {sections.map(s => (
              <li key={s.id}>
                <a href={`#${s.id}`} style={{ color: 'var(--primary-1)', textDecoration: 'none' }}
                  onClick={() => setOpenToc(false)}>
                  {s.title}
                </a>
              </li>
            ))}
          </ol>
        )}
      </div>

      {/* Section 1 */}
      <Section id="s1" title="1) Introduction">
        <p>
          The purpose of this policy is to ensure that research funded by the National Institutes of Health (NIH) is
          designed, conducted, and reported objectively and without bias resulting from Investigator financial conflicts
          of interest (FCOI). The 2011 revised regulations are 42 CFR Part 50 Subpart F, "Promoting Objectivity in
          Research" and 45 CFR Part 94, "Responsible Prospective Contractors", which set requirements for promoting
          objectivity in Public Health Service (PHS)-funded research for grants, cooperative agreements, and research
          contracts, respectively. The regulations do not apply to SBIR or STTR Phase I applications or awards. This
          policy implements the regulatory requirements for PHS/NIH grants and cooperative agreements.
        </p>
        <p>
          ZwiCoat Materials Innovations, LLC ("ZCMI," "the Company," "the Institution") adopts this policy for all
          Investigators (as defined below) engaged in PHS/NIH-funded research. It establishes processes to identify,
          disclose, and manage Investigator financial conflicts of interest to protect research integrity, ensure the
          safety of human and animal subjects, and maintain public trust in PHS/NIH-supported research.
        </p>
      </Section>

      {/* Section 2 */}
      <Section id="s2" title="2) Applicability">
        <p>
          This policy implements the regulatory requirements provided in 42 CFR Part 50 Subpart F for grants and
          cooperative agreements issued by the NIH. This policy applies to individuals who meet the regulatory
          definition of "Investigator" (as defined below) who are planning to participate in or who participate in
          PHS/NIH-funded research.
        </p>
      </Section>

      {/* Section 3 */}
      <Section id="s3" title="3) Definitions">
        <DefinitionItem term="Financial Conflict of Interest (FCOI)">
          A significant financial interest that is related to the PHS/NIH-funded research (i.e., the SFI could be
          affected by the research or the SFI is in an entity whose financial interest could be affected by the
          research) and could directly and significantly affect the design, conduct, or reporting of PHS-funded research.
        </DefinitionItem>
        <DefinitionItem term="Financial Interest">
          Anything of monetary value, whether or not its value is readily ascertainable.
        </DefinitionItem>
        <DefinitionItem term="Institutional Responsibilities">
          The professional responsibilities of an Investigator on behalf of ZCMI, which may include activities such
          as research, research consultation and collaboration, coatings formulation, materials characterization,
          substrate testing, product development, product testing and validation, manufacturing process development,
          development of datasets, models, or systems, customer technical support, collaboration with device
          manufacturers, intellectual property and patent development, fundraising, publication and communication of
          research results, and other professional services performed on behalf of ZCMI.
        </DefinitionItem>
        <DefinitionItem term="Designated Official (DO)">
          The individual appointed by ZCMI to solicit and review disclosures of significant financial interests,
          determine FCOIs in accordance with 42 CFR 50.604(f) and this policy, and develop management plans for
          identified FCOIs. The President and Chief Technology Officer serves as the Designated Official. In cases
          where the DO has a disclosed SFI related to the research under review, or where additional independence is
          warranted, the DO will recuse themselves and an alternate qualified designee or external advisor may be
          appointed. The use of such alternative review arrangements will be documented.
        </DefinitionItem>
        <DefinitionItem term="Institution">
          Any public or private organization, domestic or foreign (excluding a federal agency) that is applying for
          or receives PHS/NIH research funding.
        </DefinitionItem>
        <DefinitionItem term="Investigator">
          The Project Director (PD) or Principal Investigator (PI), and any other person, regardless of title or
          position, who is responsible for the design, conduct, or reporting of research funded by PHS/NIH or
          proposed for such funding, which may include, for example, collaborators or consultants. The Institution
          will consider the individual's role, rather than their title, and degree of independence in carrying out
          the work when making this determination.
        </DefinitionItem>
        <DefinitionItem term="Manage">
          Taking action to address a financial conflict of interest, which can include reducing or eliminating the
          financial conflict of interest, to ensure, to the extent possible, that the design, conduct, and reporting
          of research will be free from bias.
        </DefinitionItem>
        <DefinitionItem term="Research">
          A systematic investigation, study, or experiment designed to develop or contribute to generalizable
          knowledge relating broadly to public health, including behavioral and social-sciences research. The term
          encompasses basic and applied research and product development, and includes any such activity for which
          research funding is available from a PHS Awarding Component through a grant, cooperative agreement, or
          other statutory authority.
        </DefinitionItem>
        <DefinitionItem term="PHS-Funded Research">
          Any activity supported by a Public Health Service (PHS) Awarding Component through a grant, cooperative
          agreement, or contract, whether funded under the PHS Act or other statutory authority.
        </DefinitionItem>
        <DefinitionItem term="PHS">
          The Public Health Service of the U.S. Department of Health and Human Services, and any components of the
          PHS to which the authority involved may be delegated, including the National Institutes of Health (NIH).
        </DefinitionItem>
        <DefinitionItem term="NIH">
          The biomedical research agency within the Public Health Service (PHS) that funds and conducts research to
          improve health and advance scientific knowledge.
        </DefinitionItem>
        <DefinitionItem term="Senior/Key Personnel">
          The PD/PI and any other individual identified as senior/key personnel by the Institution in a grant
          application, progress report, or other submission to PHS/NIH. For this policy, the term applies
          specifically to the public accessibility requirement described in Section 9.
        </DefinitionItem>

        <p style={{ fontWeight: '600', marginTop: '0.5rem' }}>Significant Financial Interest (SFI):</p>
        <p><strong>1)</strong> A domestic or foreign financial interest of the Investigator (and those of the
          Investigator's spouse, domestic partner, and dependent children) that reasonably appears to be related to
          the Investigator's institutional responsibilities, consisting of one or more of the following:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li><strong>Publicly traded entity:</strong> An SFI exists if the total of remuneration received in the
            previous 12 months and the value of any equity interest on the disclosure date exceeds $5,000.
            Remuneration includes salary and payments for services (e.g., consulting fees, honoraria, paid
            authorship). Equity interest includes stock, stock options, or other ownership interests.</li>
          <li><strong>Non-publicly traded entity:</strong> An SFI exists if the aggregated value of remuneration
            received in the 12 months preceding disclosure exceeds $5,000, or if the Investigator (or their spouse
            or dependent children) holds any equity interest.</li>
          <li><strong>Intellectual property:</strong> An SFI exists if receipt of income related to intellectual
            property rights or interests (e.g., patents, copyrights) exceeds $5,000 during the 12 months preceding
            disclosure.</li>
        </ul>
        <p><strong>2)</strong> Investigators must disclose any reimbursed or sponsored travel related to their
          institutional responsibilities in excess of $5,000 in the previous 12 months, including at minimum the
          purpose, sponsor or organizer, destination, and duration of each trip. This requirement does not apply to
          travel reimbursed or sponsored by a U.S. federal, state, or local government agency; a U.S. Institution
          of Higher Education; an academic teaching hospital; a medical center; or a research institute affiliated
          with a U.S. Institution of Higher Education.</p>
        <p><strong>3)</strong> SFI does <em>not</em> include, and investigators are not required to disclose:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>Salary, royalties, or other remuneration paid by ZCMI to the Investigator if currently employed or
            appointed by ZCMI, including intellectual property rights assigned to ZCMI and agreements to share
            royalties related to those rights.</li>
          <li>Any ownership interest in ZCMI held by the Investigator, since ZCMI is a commercial or for-profit
            organization.</li>
          <li>Income from investment vehicles such as mutual funds and retirement accounts, provided the Investigator
            does not directly control the investment decisions for those vehicles.</li>
          <li>Income from seminars, lectures, or teaching engagements, or service on advisory committees or review
            panels, sponsored by a U.S. federal, state, or local government agency, a U.S. institution of higher
            education, an academic teaching hospital, a medical center, or a research institute affiliated with a
            U.S. institution of higher education.</li>
        </ul>

        <div style={{
          background: '#f0f7fd',
          border: '1px solid var(--primary-3)',
          borderRadius: '0.4rem',
          padding: '1rem 1.25rem',
        }}>
          <p style={{ fontWeight: '600', marginBottom: '0.5rem' }}>Foreign Financial Interests:</p>
          <p>
            Investigators must disclose all financial interests originating outside the United States, including
            income from seminars, lectures, teaching engagements, service on advisory committees or review panels,
            and reimbursed or sponsored travel, received from any foreign entity — including foreign institutions
            of higher education and foreign governments (including local or provincial governments). Disclosure is
            required when the aggregated amount of such income meets the threshold (e.g., income in excess of $5,000).
          </p>
        </div>
      </Section>

      {/* Section 4 */}
      <Section id="s4" title="4) Significant Financial Interest (SFI) Disclosure Requirements">
        <p>
          Investigators will disclose their SFIs that are related to their institutional responsibilities as defined
          in this policy. The disclosure will not be limited to an Investigator's research responsibilities or their
          funded research, as this is too narrow in scope and not consistent with the 2011 regulation. Investigator
          SFI Disclosures will be retained by the Institution as part of the record maintenance requirements.
        </p>
        <p>Investigators are required to disclose SFIs at the following times:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li><strong>At the time of application:</strong> The PI and all other Investigators must disclose their
            SFIs to the DO. Any new Investigator who joins the project after the NIH application has been submitted
            or during the course of the research must also disclose promptly and before participating, using the SFI
            Disclosure Form.</li>
          <li><strong>Annual disclosure during the award:</strong> Each Investigator must submit an updated SFI
            disclosure at least annually (on or before May 1) during the award period, including any new information
            not previously disclosed and updated details for any previously disclosed SFI.</li>
          <li><strong>Ad hoc during the award:</strong> Each Investigator must submit an updated SFI disclosure
            within 30 days of discovering or acquiring a new SFI (e.g., through purchase, marriage, or inheritance).
            Updated disclosure of reimbursed or sponsored travel must also be submitted within 30 days of each
            occurrence.</li>
        </ul>
      </Section>

      {/* Section 5 */}
      <Section id="s5" title="5) Review of SFI Disclosures">
        <p>
          The President and Chief Technology Officer serves as the Designated Official (DO) responsible for reviewing
          all SFI disclosures. In cases where the DO has a disclosed SFI related to the research under review, the
          DO will recuse themselves, and an alternate qualified designee or external advisor may be appointed. Each
          SFI will be evaluated in relation to every PHS/NIH research application or award on which the Investigator
          is responsible.
        </p>
        <p>SFI disclosures will be reviewed at the following times:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li><strong>Prior to a new award (e.g., Just-in-Time stage):</strong> The DO will review Investigator SFIs
            before NIH issues a new award. If an FCOI is identified, an FCOI report will be submitted to NIH via the
            eRA Commons FCOI Module prior to any expenditure of funds.</li>
          <li><strong>Annual SFI disclosure:</strong> The DO will review annual updates to determine whether changes
            to an existing management plan are needed. Any modifications will be reflected in the next Annual FCOI
            report submitted to NIH.</li>
          <li><strong>Ad hoc basis during the award:</strong> If a new Investigator joins a project or an existing
            Investigator acquires a new SFI, the DO will, within 60 days: (1) review the disclosure; (2) determine
            whether it is related to the PHS/NIH-funded research; (3) determine whether an FCOI exists; and if so,
            (4) implement at least an interim management plan. An FCOI report will be submitted to NIH within 60
            days of identifying the FCOI.</li>
        </ul>
      </Section>

      {/* Section 6 */}
      <Section id="s6" title="6) Relatedness of SFIs to PHS/NIH-Funded Research and FCOI">
        <p>
          The DO is responsible for assessing the relatedness of SFIs to NIH-funded research and determining when
          they constitute an FCOI.
        </p>
        <p>
          <strong>Relatedness Test:</strong> An SFI is considered "related" when the DO reasonably determines that
          the SFI could be affected by the PHS/NIH-funded research, or the SFI is in an entity whose financial
          interests could be affected by the PHS/NIH-funded research. The DO may consult with the Investigator when
          making this assessment.
        </p>
        <p>
          <strong>FCOI Determination:</strong> An FCOI exists when the DO reasonably determines that the SFI could
          directly and significantly affect the design, conduct, or reporting of the PHS/NIH-funded research
          ("significantly" meaning that the financial interest would have a material effect on the research).
        </p>
      </Section>

      {/* Section 7 */}
      <Section id="s7" title="7) Management of SFIs that Pose an FCOI">
        <p>
          When an FCOI is identified, the DO will determine and implement management strategies to ensure the
          research is conducted objectively. Examples of management conditions include, but are not limited to:
        </p>
        <ol style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>Public disclosure of the FCOI (e.g., in publications, presentations, to study personnel, to the IRB,
            IACUC, or Data Safety Monitoring Board). While public posting of FCOIs is required only for senior/key
            personnel, the DO may require disclosure of any Investigator's FCOI as a condition of a management plan.</li>
          <li>For human subjects research, disclosure of the FCOI to participants in the informed consent document.</li>
          <li>Appointment of an independent monitor to protect against bias in the design, conduct, and reporting of
            the research.</li>
          <li>Modification of the research plan.</li>
          <li>Change of personnel roles or removal from portions of the research.</li>
          <li>Reduction or elimination of the financial interest (e.g., divesting equity).</li>
          <li>Severance of relationships creating the conflict.</li>
        </ol>
        <p>
          The DO will communicate the determination and the management plan in writing to the Investigator and the
          appropriate supervisor. No expenditures on an NIH award may occur until the Investigator has met all
          disclosure requirements and agreed in writing to comply with the management plan. The DO will submit an
          FCOI report to NIH via the eRA Commons FCOI Module.
        </p>
        <p>
          In addition to Investigator FCOIs, ZCMI recognizes that certain financial interests at the institutional
          level — including company equity, intellectual property interests, or financial relationships of senior
          leadership — may present potential conflicts related to PHS/NIH-funded research. Such interests will be
          evaluated and managed as appropriate to ensure the objectivity of the research.
        </p>
      </Section>

      {/* Section 8 */}
      <Section id="s8" title="8) Monitoring Investigator Compliance">
        <p>
          ZCMI will monitor Investigator compliance with the management plan for the duration of the NIH award.
          FCOIs must be disclosed in publications, presentations, and other communications. Investigators must also
          disclose the FCOI in writing to study personnel and provide a copy of this disclosure to the DO for
          recordkeeping.
        </p>
      </Section>

      {/* Section 9 */}
      <Section id="s9" title="9) Public Accessibility of the FCOI Policy and FCOIs Held by Senior/Key Personnel">
        <p>
          <strong>FCOI Policy:</strong> A copy of this FCOI policy is available on ZCMI's public website at{' '}
          <a href="https://zwicoat.com/fcoi" style={{ color: 'var(--primary-1)' }}>zwicoat.com/fcoi</a>, as
          required by Section 4.1.10 of the NIH Grants Policy Statement. A copy of this policy has also been
          submitted to the NIH via the eRA Commons Institution Profile (IPF) Module.
        </p>
        <p>
          <strong>Identified FCOIs held by Senior/Key Personnel:</strong> Before any funds are spent under an NIH
          award, ZCMI will ensure public accessibility by providing a written response within five business days to
          requests for information about any SFI that meets all three of the following criteria:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>The SFI was disclosed and is still held by Senior/Key Personnel.</li>
          <li>ZCMI has determined that the SFI is related to the NIH-funded research.</li>
          <li>ZCMI has determined that the SFI constitutes an FCOI.</li>
        </ul>
        <p>When applicable, ZCMI will make available at minimum:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>Investigator's name, title, and role with respect to the research project</li>
          <li>Name of the entity in which the SFI is held</li>
          <li>Nature of the SFI</li>
          <li>Approximate dollar value of the SFI in the following ranges: $0–$4,999; $5,000–$9,999;
            $10,000–$19,999; amounts between $20,000–$100,000 by increments of $20,000; amounts above $100,000 by
            increments of $50,000; or a statement that the value cannot be readily determined.</li>
        </ul>
        <p>
          This information will be updated at least annually and within 60 days of the institution's identification
          of a new FCOI, and will remain available for at least three years from the most recent update.
        </p>
      </Section>

      {/* Section 10 */}
      <Section id="s10" title="10) Reporting Identified Financial Conflicts of Interest">
        <p>
          Prior to spending any funds under an NIH-funded award, ZCMI will submit an identified FCOI report to NIH
          for any Investigator's SFI determined to be an FCOI, and will ensure that the Investigator has agreed to
          and begun implementing the associated management plan.
        </p>
        <p>
          ZCMI will designate an institutional official to act as the FCOI Signing Official (FCOI SO) in the eRA
          Commons FCOI Module. FCOI reports are submitted only when an award is active and an FCOI has been
          identified. Instructions for preparing and submitting FCOI reports are available in the{' '}
          <a href="https://www.era.nih.gov/files/fcoi_user_guide.pdf" target="_blank" rel="noopener noreferrer"
            style={{ color: 'var(--primary-1)' }}>NIH eRA Commons FCOI Module User Guide</a>.
        </p>

        {/* Summary chart */}
        <div style={{ overflowX: 'auto', marginTop: '1rem' }}>
          <table style={{
            width: '100%', borderCollapse: 'collapse', fontSize: '0.9rem',
            border: '1px solid var(--grey-light)',
          }}>
            <thead>
              <tr style={{ background: 'var(--primary-1)', color: 'white' }}>
                <th style={th}>Report Type</th>
                <th style={th}>Content Required</th>
                <th style={th}>When Required</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={td}><strong>New FCOI Report</strong> (Initial)</td>
                <td style={td}>Grant number; PI; name of entity with FCOI; nature of FCOI; value of financial
                  interest (in required increments); description of how the interest relates to the research; key
                  elements of the management plan.</td>
                <td style={td}>Prior to expenditure of funds on a new award; within 60 days of identifying any new
                  FCOI during the award period.</td>
              </tr>
              <tr style={{ background: '#f8fafc' }}>
                <td style={td}><strong>Annual FCOI Report</strong></td>
                <td style={td}>Status of the FCOI (whether still being managed or no longer exists) and any changes
                  to the management plan.</td>
                <td style={td}>Submitted annually at the same time as the annual progress report, multi-year
                  progress report, or at the time of a grant extension.</td>
              </tr>
              <tr>
                <td style={td}><strong>Revised FCOI Report</strong></td>
                <td style={td}>Updates to a previously submitted FCOI report describing actions to manage the FCOI
                  going forward or revisions to the original report.</td>
                <td style={td}>Following a retrospective review when noncompliance with the regulation is identified,
                  if applicable.</td>
              </tr>
              <tr style={{ background: '#f8fafc' }}>
                <td style={td}><strong>Mitigation Report</strong></td>
                <td style={td}>Project number; project title; contact PI/PD; name of Investigator with FCOI; name
                  of entity with FCOI; reason for review; detailed methodology, findings, and conclusions.</td>
                <td style={td}>After a retrospective review when bias is found.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Section>

      {/* Section 11 */}
      <Section id="s11" title="11) Training Requirements for Investigators">
        <p>
          Each Investigator will be informed of ZCMI's FCOI Policy and trained on their responsibility to disclose
          foreign and domestic SFIs. Training must be completed before an Investigator engages in PHS/NIH-funded
          research, at least once every four years, and promptly when any of the following occur:
        </p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>ZCMI revises this policy or related procedures in a way that affects Investigator requirements.</li>
          <li>An Investigator is new to ZCMI research under an NIH award (training must be completed before
            participating).</li>
          <li>ZCMI determines that an Investigator has not complied with this policy or with a management plan
            (training must be completed within 30 days as directed by the DO).</li>
        </ul>
        <p>
          To meet the NIH training requirement, ZCMI requires Investigators to complete the{' '}
          <a href="https://grants.nih.gov/policy-and-compliance/policy-topics/fcoi/fcoi-training"
            target="_blank" rel="noopener noreferrer" style={{ color: 'var(--primary-1)' }}>
            NIH FCOI Training Tutorial
          </a>. ZCMI also requires Investigators to review the{' '}
          <a href="https://www.youtube.com/watch?v=D292YZ6BX24" target="_blank" rel="noopener noreferrer"
            style={{ color: 'var(--primary-1)' }}>
            NIH Virtual Seminar on FCOI compliance
          </a>. Send the DO the date of completion by email for audit purposes.
        </p>
      </Section>

      {/* Section 12 */}
      <Section id="s12" title="12) Noncompliance With FCOI Policy and Corrective Actions">
        <p>
          If ZCMI identifies an SFI that was not disclosed, reviewed, or managed in a timely manner, the DO will,
          within 60 days: review the SFI; determine whether it is related to NIH-funded research; determine whether
          it constitutes an FCOI; and, if so, implement an interim management plan. ZCMI will also submit an FCOI
          report to NIH via the eRA Commons FCOI Module.
        </p>
        <p>In cases of noncompliance, including:</p>
        <ul style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>Failure by the Investigator to disclose an SFI later determined to constitute an FCOI,</li>
          <li>Failure by the institution to review or manage an FCOI, or</li>
          <li>Failure by the Investigator to comply with an established management plan,</li>
        </ul>
        <p>ZCMI will, within 120 days of identifying noncompliance:</p>
        <ol style={{ paddingLeft: '2rem', margin: '0.5rem 0', lineHeight: '1.9' }}>
          <li>Conduct a retrospective review of the Investigator's activities and the NIH-funded research to
            determine whether the research, or any part of it, was biased in the design, conduct, or reporting.</li>
          <li>Document the retrospective review in accordance with 42 CFR 50.605(a)(3)(ii)(B) or NIH's FAQ I.2.</li>
        </ol>
        <p>
          If bias is found, ZCMI will promptly notify NIH and submit a mitigation report as required by 42 CFR
          50.605(a)(3)(iii), including the impact of the bias on the research project and the plan of action or
          corrective steps taken to eliminate or mitigate the effect of the bias.
        </p>
        <p>
          If bias is not found following completion of the retrospective review, no further action will be taken
          unless new information is discovered. If the failure of an Investigator to comply with this policy or a
          management plan appears to have biased the design, conduct, or reporting of PHS/NIH-funded research, the
          Institution shall promptly notify the PHS/NIH Awarding Component of the corrective action taken or to be
          taken.
        </p>
      </Section>

      {/* Section 13 */}
      <Section id="s13" title="13) Clinical Research Requirements">
        <p>
          If HHS determines that a PHS-funded clinical research project evaluating the safety or effectiveness of a
          drug, medical device, or treatment was designed, conducted, or reported by an Investigator with an
          unmanaged or unreported FCOI, ZCMI will require the Investigator to disclose the conflict in every public
          presentation of the research results and to request an addendum to previously published presentations.
        </p>
      </Section>

      {/* Section 14 */}
      <Section id="s14" title="14) Subrecipient Requirements">
        <p>
          A subrecipient relationship exists when federal funds flow from or through ZCMI to another individual or
          entity that will carry out a substantive portion of a PHS-funded research project and is accountable to
          ZCMI for programmatic outcomes and compliance. Subrecipients (e.g., collaborators, consortium members,
          consultants, contractors, subcontractors, and sub-awardees) are subject to ZCMI's terms and conditions.
          ZCMI will include in each written agreement with a subrecipient terms specifying whether ZCMI's FCOI
          Policy or the subrecipient's own FCOI policy will apply.
        </p>
        <p><strong>If the subrecipient's FCOI policy applies:</strong> The subrecipient institution must certify
          that its policy complies with federal FCOI regulations. The agreement will specify the timeframe for the
          subrecipient to report identified FCOIs to ZCMI (typically within 50–55 days of identification) in time
          for ZCMI to meet NIH reporting deadlines. ZCMI's DO will then submit the subrecipient FCOI report to NIH.
        </p>
        <p><strong>If the subrecipient cannot certify compliance:</strong> The agreement will specify that ZCMI's
          FCOI Policy applies. Subrecipient Investigators must disclose their SFIs to ZCMI. When an FCOI is
          identified, ZCMI will implement a management plan, monitor compliance, and submit the required FCOI report
          to NIH via the eRA Commons FCOI Module.
        </p>
      </Section>

      {/* Section 15 */}
      <Section id="s15" title="15) Maintenance of Records">
        <p>
          ZCMI will maintain records of all Investigator financial interest disclosures, ZCMI's review and response
          to those disclosures (whether or not they resulted in a determination of an FCOI), and any actions taken
          under this policy or through retrospective review. These records will be retained for at least three years
          from the date of submission of the final expenditures report, or for longer periods as specified in 2 CFR
          200.334. ZCMI will retain these records for each competitive segment as required by regulation. Copies of
          management plans will be retained as part of the record maintenance requirements.
        </p>
      </Section>

      {/* Section 16 */}
      <Section id="s16" title="16) Enforcement Actions for Investigator Noncompliance">
        <p>
          Compliance with this policy is a condition of employment and/or participation for all applicable
          Investigators. Failure to comply with this policy — including failure to disclose Significant Financial
          Interests, failure to comply with a Conflict Management Plan, or failure to complete required training —
          may result in appropriate corrective or disciplinary actions.
        </p>
        <p>
          Such actions may include, but are not limited to, formal notification or disciplinary measures,
          restrictions on participation in research activities or use of research funds, suspension or termination
          of employment or contractual relationship, and/or disqualification from participation in Government
          Award-funded research.
        </p>
        <p>
          In addition, ZCMI will take all actions required under applicable federal regulations and sponsor
          requirements, including conducting retrospective review, implementing mitigation measures where necessary,
          and notifying the sponsor when required.
        </p>
      </Section>

      {/* Section 17 */}
      <Section id="s17" title="17) Useful FCOI and NIH Resources">
        <ul style={{ paddingLeft: '2rem', lineHeight: '2' }}>
          <li>
            NIH FCOI email:{' '}
            <a href="mailto:fcoicompliance@mail.nih.gov" style={{ color: 'var(--primary-1)' }}>
              fcoicompliance@mail.nih.gov
            </a>
          </li>
          <li>
            FCOI Regulation:{' '}
            <a href="https://www.ecfr.gov/current/title-42/chapter-I/subchapter-D/part-50/subpart-F"
              target="_blank" rel="noopener noreferrer" style={{ color: 'var(--primary-1)' }}>
              42 CFR Part 50 Subpart F – Promoting Objectivity in Research
            </a>
          </li>
          <li>
            Financial Conflict of Interest:{' '}
            <a href="https://grants.nih.gov/policy-and-compliance/policy-topics/fcoi"
              target="_blank" rel="noopener noreferrer" style={{ color: 'var(--primary-1)' }}>
              grants.nih.gov/policy-and-compliance/policy-topics/fcoi
            </a>
          </li>
          <li>
            FCOI Training:{' '}
            <a href="https://grants.nih.gov/policy-and-compliance/policy-topics/fcoi/fcoi-training"
              target="_blank" rel="noopener noreferrer" style={{ color: 'var(--primary-1)' }}>
              grants.nih.gov/policy-and-compliance/policy-topics/fcoi/fcoi-training
            </a>
          </li>
          <li>NIH "Welcome Wagon" Letter: Information for New Recipient Organizations</li>
        </ul>
      </Section>

      {/* Section 18 */}
      <Section id="s18" title="18) Point of Contact">
        <p>
          If you have a question related to the FCOI Policy of ZCMI, or would like to disclose a financial interest,
          contact us using the information below:
        </p>
        <address style={{ marginTop: '0.75rem', fontStyle: 'normal', lineHeight: '1.9' }}>
          <strong>Kameron Hansen, Ph.D.</strong><br />
          President and Chief Technology Officer<br />
          ZwiCoat Materials Innovations, LLC<br />
          2635 Johnsons XING NE<br />
          Solon, IA 52333<br />
          Phone:{' '}
          <a href="tel:+19176094598" style={{ color: 'var(--primary-1)' }}>(917) 609-4598</a><br />
          Email:{' '}
          <a href="mailto:kameronh@zwicoat.com" style={{ color: 'var(--primary-1)' }}>
            kameronh@zwicoat.com
          </a>
        </address>
      </Section>

    </div>
  );
};

const th = {
  padding: '0.6rem 0.85rem',
  textAlign: 'left',
  fontWeight: '600',
  fontSize: '0.85rem',
  borderBottom: '1px solid rgba(255,255,255,0.3)',
};

const td = {
  padding: '0.65rem 0.85rem',
  verticalAlign: 'top',
  borderBottom: '1px solid var(--grey-light)',
  lineHeight: '1.6',
};

const Section = ({ id, title, children }) => (
  <section id={id} style={{ marginBottom: '2.25rem', scrollMarginTop: '80px' }}>
    <h2 style={{
      fontSize: '1.05rem',
      fontWeight: '700',
      color: 'var(--primary-1)',
      borderBottom: '1px solid var(--grey-light)',
      paddingBottom: '0.4rem',
      marginBottom: '0.9rem',
      textTransform: 'uppercase',
      letterSpacing: '0.04em',
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
